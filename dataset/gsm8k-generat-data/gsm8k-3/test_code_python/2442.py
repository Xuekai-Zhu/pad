def solution():
    """Nancy can hula hoop for 10 minutes.  Casey can hula hoop 3 minutes less than Nancy.  Morgan can hula hoop three times as long as Casey.  How long can Morgan hula hoop?"""
    # Define the amount of time Nancy can hula hoop
    nancy_time = 10

    # Define the amount of time Casey can hula hoop
    casey_time = nancy_time - 3

    # Define the amount of time Morgan can hula hoop
    morgan_time = casey_time * 3

    # Display how long Morgan can hula hoop
    result = morgan_time
    return result

print(solution())