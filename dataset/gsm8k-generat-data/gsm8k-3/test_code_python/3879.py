def solution():
    """Bruce can make 15 batches of pizza dough using a sack of flour. If he uses 5 sacks of flour per day, how many pizza doughs can he make in a week?"""
    # Define the number of batches of pizza dough that can be made with one sack of flour
    BATCHES_PER_SACK = 15

    # Define the number of sacks of flour used per day
    SACKS_PER_DAY = 5

    # Calculate the number of pizza doughs that can be made in one day
    doughs_per_day = BATCHES_PER_SACK * SACKS_PER_DAY

    # Calculate the number of pizza doughs that can be made in one week
    doughs_per_week = doughs_per_day * 7

    # Display the number of pizza doughs that can be made in one week
    result = doughs_per_week
    return result

print(solution())