def solution():
    """Marty and Biff were both running for student council president. A poll was taken to see how the candidate’s campaigns were going. 45% of the people polled said they were voting for Biff and 8% were undecided. The rest said they are voting for Marty. If 200 people were polled, how many said they are voting for Marty?"""
    # Calculate the percentage of people voting for Marty
    marty_percent = 100 - 45 - 8

    # Calculate the number of people voting for Marty
    marty_count = int((marty_percent / 100) * 200)

    # Display the number of people voting for Marty
    result = marty_count
    return result

print(solution())