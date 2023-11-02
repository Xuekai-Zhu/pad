def solution():
    # Calculate the total number of sweets in the packet
    total_sweets = 30 + 40 + 50

    # Calculate the number of each flavor of sweet that Aaron eats
    cherry_sweets_eaten = 30 / 2  # Half of the cherry-flavored sweets
    strawberry_sweets_eaten = 40 / 2  # Half of the strawberry-flavored sweets
    pineapple_sweets_eaten = 50 / 2  # Half of the pineapple-flavored sweets

    # Calculate the total number of sweets Aaron eats
    total_sweets_eaten = cherry_sweets_eaten + strawberry_sweets_eaten + pineapple_sweets_eaten

    # Subtract the sweets Aaron eats and gives away from the total number of sweets
    sweets_remaining = total_sweets - total_sweets_eaten - 5

    result = sweets_remaining
    return result

print(solution())