import os
from typing import Optional
from dotenv import load_dotenv
import openai

class OpenAIClient:
    def __init__(self):
        load_dotenv()
        openai.api_key = os.getenv("OPENAI_API_KEY")

    async def generate_text(
        self,
        model: str = "text-davinci-003",
        prompt: str = "",
        temperature: float = 0.7,
        max_tokens: Optional[int] = None,
        top_p: Optional[float] = None,
        frequency_penalty: Optional[float] = None,
        presence_penalty: Optional[float] = None,
    ):
        """
        Generates text using the OpenAI API.

        Args:
            model: The OpenAI model to use (e.g., "text-davinci-003").
            prompt: The text prompt to use for generation.
            temperature: Controls the randomness of the generated text.
            max_tokens: The maximum number of tokens to generate.
            top_p: The probability threshold for sampling from the model's vocabulary.
            frequency_penalty: Penalty for generating text that repeats frequently.
            presence_penalty: Penalty for generating text that is too similar to the prompt.

        Returns:
            A string containing the generated text.

        Raises:
            openai.error.OpenAIError: If there is an error communicating with the OpenAI API.
        """
        try:
            response = await openai.Completion.acreate(
                engine=model,
                prompt=prompt,
                temperature=temperature,
                max_tokens=max_tokens,
                top_p=top_p,
                frequency_penalty=frequency_penalty,
                presence_penalty=presence_penalty,
            )
            return response.choices[0].text
        except openai.error.OpenAIError as e:
            raise Exception(f"OpenAI API Error: {e}")