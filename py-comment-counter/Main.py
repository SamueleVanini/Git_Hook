"""
sys -> module for command line argument
Comment_Control -> module for the validation of a comment
Comments_Distribution -> module for the control of comment distribution into the code
"""
import sys
from Components import Comment_Control, Comments_Distribution


def main(file_input):
    """
    Main of program
    :param file_input: file with the comments to count
    :return: comments percentage
    """
    file = open(file_input, 'r')
    result_list = file_reader(file)
    file.close()
    try:
        print((float(result_list[1])/float(result_list[0]))*100)
    except ZeroDivisionError:
        print('file empty')
    # return(result_list[1]/result_list[0]*100)


def file_reader(file):
    """
    Function for read the file and check for comment
    :param file: file to read
    :return result_result: list with line_count and comment_count
    """
    comment_count = 0
    line_count = 0
    pydoc_line_counter = 0
    first_line_comment = False
    comment_block = False
    function_start = False
    for line in file:
        line_count += 1
        line = line.replace('\n', '')
        try:
            # control if the line is the start of a function
            if Comments_Distribution._function_comment(line):
                function_start = True
            # control if the line is the start of a multi line comments block
            elif Comment_Control._is_start_comment(line) and comment_block is False:
                if Comment_Control._is_pydoc(line):
                    line_count -= 1
                    function_start = False
                    comment_block = True
                else:
                    first_line_comment = True
                    pydoc_line_counter += 1
                    comment_count += 1
                    comment_block = True
                    function_start = False
            # control is the line is a comment inside a multi line comments block
            elif comment_block is True:
                first_line_comment = False
                if Comment_Control._is_pydoc(line):
                    line_count -= 1
                elif Comment_Control._is_comment(line):
                    comment_count += 1
                    pydoc_line_counter += 1
            # control if the line is a single comment line (comments start with '#')
            elif Comment_Control._is_hashtag_comment(line) and comment_block is False:
                if Comment_Control._is_comment(line):
                    comment_count += 1
            elif function_start:
                print('pydoc assente')
                function_start = False
            # control if the line is the end of multi line comments block
            if Comment_Control._is_end_comment(line) and not first_line_comment:
                comment_block = False
                line_count -= pydoc_line_counter
                comment_count -= pydoc_line_counter
                pydoc_line_counter = 0
                line_count -= 1
            if line == '':
                line_count -= 1
        except IndexError:
            pass

    result_list = [line_count, comment_count]
    return result_list

if __name__ == '__main__':
    main(sys.argv[1])
