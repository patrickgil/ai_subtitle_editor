'''
Central file used to call functions from external files.
(OpenAI API error handling is not currently included)

- The output filename is gathered from the input
    - The output language is pre-defined as English: can be edited in Global Constants
- The console output is printed
    - Includes input name/language and output name/language
- The message given to the API is pre-defined to simply ask for a translation from the
  input language to the output language
- The start time is recorded
- A loop runs through the 'blocks' of lines from the srt file to send small requests to the API
    - The output is appended to an initially empty string
    - The current block being processed is ouput to the console
- The output string is then printed to an .srt file
'''

# =============================================================================================
# =========IMPORTS=============================================================================
# Local imports
import gather_srt_files as srt
import api_calls as api
import lang_codes as lang
# Global imports
import sys
import time

# =============================================================================================
# =========CONSTANTS===========================================================================
FILENAME = sys.argv[1]
OUTPUT_LANGUAGE = lang.language_codes['en']
OUTPUT_LANGUAGE_CODE = lang.language_dict['English']
OUTPUT_STRING = ''

# =============================================================================================
# =========FUNCTIONS===========================================================================


def create_filename(srt_language_code: str):
    """
    Function to take in filename and output language to create the filename

    :param srt_language_code: output ISO language code
    :return: output srt filename
    """
    if len(srt_language_code) == 2:
        output_filename = '{}.{}.srt'.format(FILENAME[:-7], OUTPUT_LANGUAGE_CODE)
    elif len(srt_language_code) == 4:
        output_filename = '{}.{}.srt'.format(FILENAME[:-10], OUTPUT_LANGUAGE_CODE)
    return output_filename


def main():
    """
    Function to execute the program
    """
    # Gather Language and Filename
    srt_language = srt.gather_langauge(FILENAME)
    srt_language_code = lang.language_dict[srt_language]
    output_file = create_filename(srt_language_code)

    # Collect the lines from the .srt file
    srt_lines = srt.read_file(FILENAME)
    list_of_lines = srt.split_file(srt_lines)

    # Print information
    print('Input .srt file:    {}'.format(FILENAME))
    print('Input Language:     {}'.format(srt_language))
    print('Output Language:    {}'.format(OUTPUT_LANGUAGE))
    print('Output Filename:    {}'.format(output_file))
    print('------------------------------------------------------------------------------')

    # Setup message for API Call
    message = 'Translate the following from {} to {}:\n'.format(srt_language, OUTPUT_LANGUAGE)
    # Iterate upon the blocks of lines
    # Each block contains 50 lines from the .srt file
    total = len(list_of_lines)
    start_time = time.time()
    OUTPUT_STRING = ''
    for iteration, lines in enumerate(list_of_lines):
        srt_string = ''
        for line in lines:
            srt_string += line
        if iteration > 0:
            print('Waiting for 15 Seconds')
            time.sleep(15)
        print('Calling API: Call: {} out of {}'.format(iteration+1, total))
        call_api = api.call_gpt(message, srt_string)
        print('API Called Successfully')
        print('------------------------------------------------------------------------------')
        OUTPUT_STRING += '\n' + call_api
    end_time = time.time()
    print('API Call Completed in {} seconds'.format(int(end_time-start_time)))
    print('Writing to file: {}'.format(output_file))
    srt.write_file(output_file, OUTPUT_STRING)
    print('File Write Successful')


if __name__ == "__main__":
    main()
