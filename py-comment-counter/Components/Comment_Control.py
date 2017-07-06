"""
configparser -> module for the parse of .ini file
keyword -> module for the keywords of python
os -> module for the interaction with the Operation System
"""
import configparser
import keyword
import os

config = configparser.ConfigParser()
config.read(os.path.join('py-comment-counter', 'config_script', 'config.ini'))
num_max_of_python_word_for_comment = config.getint('Comments_Counter', 'num_max_of_python_word_for_comment')


def _is_comment(line):
    """
    Check if the words in the line are comments or code
    :param line: line to control
    :return True/False: boolean to indicate if the line is comment or not
    """
    code_counter = 0
    code_word = keyword.kwlist
    for word in line:
        if word == code_word:
            code_counter += 1
    return code_counter < num_max_of_python_word_for_comment


def _is_start_comment(line):
    """
    Check if the line is the start of a multi line comment
    :param line: line to control
    :return True/False: boolean to indicate if the line is the end of a multi line comment
    """
    line = line.strip(' \t\n\r')
    return bool(line.startswith("'''") or line.startswith('"""'))


def _is_end_comment(line):
    """
    Check if the line is the end of a multi line comment
    :param line: line to control
    :return True/False: boolean to indicate if the line is the end of a multi line comment
    """
    return bool((line.endswith("'''") or line.endswith('"""')))


def _is_hashtag_comment(line):
    """
    Check if the '#' is a comment or into a string
    :param line: line to control
    :return True/False: boolean to indicate if '#' is a comment or into a string
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
