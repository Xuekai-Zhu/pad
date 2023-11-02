def solution():
    """A bird eats 7 berries a day. Samuel has 5 birds. How many berries do Samuel's birds eat in 4 days?"""
    # Define the number of berries eaten by a bird per day
    berries_per_bird = 7

    # Define the number of birds Samuel has
    num_birds = 5

    # Calculate the total number of berries eaten by Samuel's birds in 4 days
    total_berries = berries_per_bird * num_birds * 4

    # return the result
    result = total_berries
    return result

print(solution())