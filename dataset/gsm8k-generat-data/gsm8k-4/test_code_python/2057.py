def solution():
    """Jack, who weighs 60 pounds, wants to play on the see-saw with his cousin Anna, who weighs 40 pounds. How many 4-pound rocks does Jack need to hold to make their weights equal?"""
    # Define the weights of Jack and Anna
    jack_weight = 60
    anna_weight = 40

    # Calculate the difference in weight
    weight_diff = abs(jack_weight - anna_weight)

    # Calculate the number of 4-pound rocks needed to balance the weight
    num_rocks = weight_diff / 4

    # Round up to the nearest integer
    num_rocks = int(num_rocks + 0.5)

    # Return the result
    result = num_rocks
    return result

print(solution())