def solution():
    """Nancy can hula hoop for 10 minutes. Casey can hula hoop 3 minutes less than Nancy. Morgan can hula hoop three times as long as Casey. How long can Morgan hula hoop?"""
    nancy_time = 10
    casey_time = nancy_time - 3
    morgan_time = casey_time * 3
    result = morgan_time
    return result

print(solution())