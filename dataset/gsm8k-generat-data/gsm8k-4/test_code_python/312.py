def solution():
    """Farmer Brown raises emus, large birds. His flock has a total of 60 heads and legs. How many emus are in his flock?"""
    # Define the number of legs per emu
    legs_per_emu = 2

    # Define the total number of heads and legs
    total_heads_legs = 60

    # Calculate the number of emus in the flock
    emus = (total_heads_legs / (legs_per_emu + 1))

    # Return the result
    result = emus
    return result

print(solution())