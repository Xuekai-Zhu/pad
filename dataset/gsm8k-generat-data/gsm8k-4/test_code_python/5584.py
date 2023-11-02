def solution():
    """Marty and Biff were both running for student council president. A poll was taken to see how the candidate’s campaigns were going. 45% of the people polled said they were voting for Biff and 8% were undecided. The rest said they are voting for Marty. If 200 people were polled, how many said they are voting for Marty?"""
    # Define the percentages of voters for Biff and undecided
    biff_percentage = 0.45
    undecided_percentage = 0.08

    # Calculate the percentage of voters for Marty
    marty_percentage = 1 - biff_percentage - undecided_percentage

    # Calculate the number of people voting for Marty
    marty_count = int(marty_percentage * 200)

    result = marty_count
    return result

print(solution())