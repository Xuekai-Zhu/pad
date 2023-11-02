def solution():
    adult_price = 7
    child_price = 3

    # Let's assume there are x adults
    # Then there are 3x children
    # The total number of people is x + 3x = 4x
    # The total revenue is 7x + 3(3x) = 16x
    # We know the total revenue is $6000
    # So, 16x = 6000
    # Therefore, x = 375 (number of adults)

    num_children = 3 * 375
    num_people = 375 + num_children
    result = num_people
    return result

print(solution())