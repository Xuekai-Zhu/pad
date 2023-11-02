def solution():
    """Every 4 weeks, Helen hand washes her silk pillowcases.  It takes 30 minutes to hand wash all of them.  In 1 year, how much time does Helen spend hand washing her pillowcases?"""
    # Define the number of minutes to hand wash the pillowcases
    MINUTES_PER_WASH = 30

    # Define the number of pillowcases and the frequency of washing
    frequency = 4 # wash every 4 weeks
    num_pillowcases = 2 # assume Helen has 2 silk pillowcases

    # Calculate the number of washes in a year
    num_washes = 52 / frequency

    # Calculate the total time spent hand washing the pillowcases in a year
    total_time = num_washes * num_pillowcases * MINUTES_PER_WASH

    # Display the total time spent hand washing the pillowcases in a year
    result = total_time
    return result

print(solution())