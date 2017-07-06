def _function_comment(line):
    """
    Check if the line is the start of a function
    :param line: line to control
    :return True/False: boolean to indicate if the line is the start of a function
    """
    return True if line.startswith('def') else False
