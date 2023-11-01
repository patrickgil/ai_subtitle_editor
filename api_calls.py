'''
Module to access the OpenAI api
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
    completion = openai.ChatCompletion.create(
        model=GPT_VERSION,
        messages=[{
                "role": "user",
                "content": message_input + srt_input},
        ],
    )
    return completion.choices[0].message.content
