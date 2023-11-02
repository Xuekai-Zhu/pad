def solution():
    """Nancy can hula hoop for 10 minutes. Casey can hula hoop 3 minutes less than Nancy. Morgan can hula hoop three times as long as Casey. How long can Morgan hula hoop?"""
    # Define Nancy's hula hooping time
    nancy_time = 10

    # Define Casey's hula hooping time
    casey_time = nancy_time - 3

    # Define Morgan's hula hooping time
    morgan_time = casey_time * 3

    # return the result
    result = morgan_time
    return result

print(solution())