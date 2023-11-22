def solution():
    
    # Define the number of marshmallows in the bag
    total_marshmallows = 35

    # Define the number of S'mores each person can make
    john_marshmallows = 9
    desean_marshmallows = 9

    # Subtract the number of marshmallows that were dropped
    remaining_marshmallows = total_marshmallows - 3

    # Calculate the number of S'mores each kid can have
    s_marshmallows_per_kid = remaining_marshmallows // 2

    # Display the number of S'mores each kid can have
    result = s_marshmallows_per_kid
    return result

print(solution())