def solution():
    """Barkley gets 10 new dog bones at the beginning of the month. After 5 months, he has 8 bones available and has buried the rest. How many bones has he buried?"""
    # Define the initial number of dog bones
    num_bones = 10

    # Define the number of months
    num_months = 5

    # Calculate the number of bones left after 5 months
    bones_left = 8

    # Calculate the number of bones buried
    bones_buried = (num_bones - bones_left) * num_months

    result = bones_buried
    return result

print(solution())