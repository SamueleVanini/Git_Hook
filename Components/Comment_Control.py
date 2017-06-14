"""
configparser -> module for the parse of .ini file
keyword -> module for the keyword of python
"""
import configparser
import keyword


def _is_comment(line):
    """
    Check if the words into the line are comments or code
    :param line: line to control
    :return True/False: boolean to indicate if the line is comment or not
    """
    config = configparser.ConfigParser()
    config.read("config_script/config.ini") # MP: qui meglio usare os.path.join, in modo da renderlo multipiattaforma
    NUM_KEY_WORD_COMM = config.getint('Comments_Counter', 'Num_Key_Word_Comm')
    code_counter = 0
    code_word = keyword.kwlist
    for word in line:
        if word == code_word:
            code_counter += 1
    return code_counter < NUM_KEY_WORD_COMM


def _is_start_comment(line):
    """
    Check if the line is the start of multi line comments
    :param line: line to control
    :return True/False: boolean to indicate if the line is the end of multi line comments
    """
    line = line.strip(' \t\n\r')
    return bool(line.startswith("'''") or line.startswith('"""'))


def _is_end_comment(line):
    """
    Check if the line is the end of multi line comments
    :param line: line to control
    :return True/False: boolean to indicate if the line is the end of multi line comments
    """
    return bool((line.endswith("'''") or line.endswith('"""')))


def _is_canc_comment(line):
    """
    Check if the '#' is for a comment or into a string
    :param line: line to control
    :return True/False: boolean to indicate if '#' is comment or into a string
    """
    comment_block = False
    for letter in line:
        if letter == '\'' or letter == '\"':
            comment_block = False if comment_block else True
        if letter == '#' and comment_block is False:
            return True
        if letter == '#' and comment_block is True:
            return False


def _is_pydoc(line):
    """
    Check if the ':' is pydoc or code
    :param line: line to control
    :return True/False: boolean to indicate if ':' is comment or code
    """
    return True if line.find(':') == len(line)-1 else False
