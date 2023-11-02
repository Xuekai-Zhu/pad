def solution():
    # Define the initial number of dog bones Barkley has
    initial_bones = 10

    # Define the number of months Barkley has had the bones
    months = 5

    # Calculate the number of bones Barkley has left
    remaining_bones = 8

    # Calculate the total number of bones Barkley has buried
    buried_bones = (initial_bones - remaining_bones) * months
    result = buried_bones
    return result

print(solution())