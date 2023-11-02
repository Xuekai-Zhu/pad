def solution():
    """Jeremy decides to take Tylenol because of the pain he is experiencing. He decides to take 1000 mg every 6 hours for 2 weeks.  How many pills do they take if they are each 500 mg?"""
    # Define the dose and the duration of intake
    dose = 1000 # in mg
    duration = 14 * 24 # in hours

    # Calculate the number of pills taken
    pills = (duration // 6) * (dose / 500)

    # Display the number of pills taken
    result = pills
    return result

print(solution())