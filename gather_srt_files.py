'''
Module to convert .srt files to usable lists of lines
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
    if '.srt' not in filename:
        sys.exit('The file input is not an .srt file. Aborting')
    elif '.srt' in filename:
        readfile = open(filename, 'r')
        lines = readfile.readlines()
        time.sleep(5)
        readfile.close()
    return lines


def split_file(lines):
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
    writefile = open(filename, 'w')
    writefile.write(lines)
    time.sleep(5)
    writefile.close()
