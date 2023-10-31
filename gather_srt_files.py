'''
Module to convert .srt files to usable lists of lines
'''

# =============================================================================================
# =========IMPORTS=============================================================================


# =============================================================================================
# =========CONSTANTS===========================================================================


# =============================================================================================
# =========FUNCTIONS===========================================================================


def read_file(filename):
    readfile = open(filename, 'r')
    lines = readfile.readlines()
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
