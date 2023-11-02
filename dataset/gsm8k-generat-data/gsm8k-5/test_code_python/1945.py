def solution():
    # Calculate how much weight has been used up by watermelon, grapes, and oranges
    used_weight = 3  # Watermelon, grapes, and oranges each weigh 1 pound
    # Calculate how much weight Diego has left in his bookbag
    remaining_weight = 20 - used_weight
    # Calculate how much weight an apple weighs
    apple_weight = 0.5  # Assume each apple weighs half a pound
    # Calculate how many apples Diego can buy
    num_apples = remaining_weight // apple_weight
    result = num_apples
    return result

print(solution())