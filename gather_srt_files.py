'''
Module to read and write .srt files
- Input language is determined from filename (user input)
- The .srt file is read and parsed into a string of lines
- Lines are split into 'blocks' of lines (50 lines per block)
- Output string is written to new .srt file
    - Filename is the same with different ISO language extention
'''

# =============================================================================================
# =========IMPORTS=============================================================================
import sys
import time
import lang_codes as lang

# =============================================================================================
# =========CONSTANTS===========================================================================


# =============================================================================================
# =========FUNCTIONS===========================================================================


def gather_langauge(filename: str):
    """
    Function that takes a proper .srt filename and determines the ISO language code

    :param filename: .srt filename (user input)
    :return: language of subtitle in filename
    """
    if filename[-7] == '.':
        lang_string = filename[-6:-4]
        try:
            langauge = lang.language_codes[lang_string]
        except KeyError:
            sys.exit('No Language specified in .srt file. Aborting')
    elif filename[-10] == '.':
        lang_string = filename[-9:-4]
        try:
            langauge = lang.language_codes[lang_string]
        except KeyError:
            sys.exit('No Language specified in .srt file. Aborting')
    else:
        sys.exit('.srt file does not have a proper language code. Aborting')
    return langauge


def read_file(filename: str):
    """
    Function to read .srt files and return the lines

    :param filename: .srt filename (user input)
    :return: all subtitle lines (includes blank new lines)
    """
    if '.srt' not in filename:
        sys.exit('The file input is not an .srt file. Aborting')
    elif '.srt' in filename:
        readfile = open(filename, 'r')
        lines = readfile.readlines()
        time.sleep(5)
        readfile.close()
    return lines


def split_file(lines):
    """
    Function to split all subtitle lines into usable 'blocks' of 50 lines

    :param lines: all subtitle lines from .srt files
    :return: list of srt line 'blocks' (50 lines)
    """
    count = 0
    start = 0
    total_lines = len(lines)
    start_final = total_lines - (total_lines % 50) - 1
    srt_lines = []
    line_lists = []
    for line in lines:
        str = line
        if count > 0:
            if count % 50 == 0:
                start = count - 50
                end = count
                line_lists.append(srt_lines[start:end])
            if len(lines) % 50 != 0:
                if count == (len(lines)-1):
                    line_lists.append(srt_lines[start_final:count])
        srt_lines.append(str)
        count += 1
    return line_lists


def write_file(filename: str, lines: str):
    """
    Function to write to .srt files

    :param filename: output filename (same as input with different ISO language code)
    :param lines: final string of lines (output from API call)
    :return: None
    """
    writefile = open(filename, 'w')
    writefile.write(lines)
    time.sleep(5)
    writefile.close()
