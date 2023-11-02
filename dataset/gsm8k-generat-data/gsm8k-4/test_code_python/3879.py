def solution():
    """Bruce can make 15 batches of pizza dough using a sack of flour. If he uses 5 sacks of flour per day, how many pizza doughs can he make in a week?"""
    # Define the number of batches of pizza dough that can be made from one sack of flour
    batches_per_sack = 15

    # Define the number of sacks of flour used per day
    sacks_per_day = 5

    # Calculate the number of batches of pizza dough that can be made in one day
    batches_per_day = batches_per_sack * sacks_per_day

    # Calculate the number of batches of pizza dough that can be made in one week
    batches_per_week = batches_per_day * 7

    # return the result
    result = batches_per_week
    return result

print(solution())