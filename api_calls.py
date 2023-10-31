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


def call_gpt(input):
    input = 'key'
    return input


completion = openai.ChatCompletion.create(
    model=GPT_VERSION,
    messages=[{
            "role": "user",
            "content": "Compose a poem that explains the concept of recursion in programming."},
    ],
)

print(completion.choices[0].message)
