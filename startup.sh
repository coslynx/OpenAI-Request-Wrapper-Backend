#!/bin/bash

# Strict error handling
set -euo pipefail

# Load environment variables
if [ -f .env ]; then
  source .env
fi

# Validate required environment variables
if [ -z "${OPENAI_API_KEY}" ]; then
  echo "Error: OPENAI_API_KEY environment variable is missing." >&2
  exit 1
fi

if [ -z "${DATABASE_URL}" ]; then
  echo "Error: DATABASE_URL environment variable is missing." >&2
  exit 1
fi

# Define project variables
PROJECT_ROOT=$(pwd)
LOG_FILE="${PROJECT_ROOT}/logs/startup.log"
PID_FILE="${PROJECT_ROOT}/logs/app.pid"

# Utility functions
log_info() {
  echo "$(date +'%Y-%m-%d %H:%M:%S') - INFO: $*"
}

log_error() {
  echo "$(date +'%Y-%m-%d %H:%M:%S') - ERROR: $*" >&2
}

cleanup() {
  if [ -f "${PID_FILE}" ]; then
    kill $(cat "${PID_FILE}") 2>/dev/null
  fi
  rm -f "${PID_FILE}"
}

# Service management functions
start_database() {
  log_info "Starting database..."
  sqlite3 database.db < database/schema.sql
  log_info "Database started."
}

start_backend() {
  log_info "Starting backend server..."
  uvicorn api.main:app --host 0.0.0.0 --port 8000 &
  store_pid $!
  log_info "Backend server started."
}

store_pid() {
  echo "$1" > "${PID_FILE}"
}

# Trap signals
trap cleanup EXIT ERR

# Main execution
check_dependencies

start_database
start_backend

# Log startup completion
log_info "Startup complete."