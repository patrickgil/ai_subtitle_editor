'''
Module to access the OpenAI api
(OpenAI API error handling is not currently included)
'''

# =============================================================================================
# =========IMPORTS=============================================================================
import os
import openai
openai.api_key = os.getenv("OPENAI_API_KEY")

# =============================================================================================
# =========CONSTANTS===========================================================================
GPT_VERSION = 'gpt-3.5-turbo'

# =============================================================================================
# =========FUNCTIONS===========================================================================


def call_gpt(message_input: str, srt_input: str):
    """
    Calls the OpenAI API

    :param message_input: prompt given by user to the API
    :param srt_input: lines from the iput .srt file
    :return: response from gpt
    """
    completion = openai.ChatCompletion.create(
        model=GPT_VERSION,
        messages=[{
                "role": "user",
                "content": message_input + srt_input},
        ],
    )
    return completion.choices[0].message.content
