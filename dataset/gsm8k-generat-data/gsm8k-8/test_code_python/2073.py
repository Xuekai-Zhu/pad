def solution():
    # Define the initial amount of jelly beans
    initial_amount = 36

    # Subtract the amount Alex ate
    remaining_amount = initial_amount - 6

    # Divide the remaining amount into 3 equal piles
    pile_weight = remaining_amount / 3

    result = pile_weight
    return result

print(solution())