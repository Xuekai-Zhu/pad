def solution():
    """A bird eats 7 berries a day. Samuel has 5 birds. How many berries do Samuel's birds eat in 4 days?"""
    # Define the number of berries that one bird eats per day
    BERRIES_PER_BIRD_PER_DAY = 7

    # Define the number of birds Samuel has
    num_birds = 5

    # Calculate the total number of berries all of Samuel's birds eat in 4 days
    total_berries = BERRIES_PER_BIRD_PER_DAY * num_birds * 4

    # Display the total number of berries
    result = total_berries
    return result

print(solution())