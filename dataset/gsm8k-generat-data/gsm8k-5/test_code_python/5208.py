def solution():
    total_price = 720  # The group pays $720 in total
    adult_price = 15  # The price of an adult ticket is $15
    child_price = 8  # The price of a child ticket is $8
    num_adults = 0
    num_children = 0

    # Find the number of adults and children in the group
    for i in range(1, 100):  # Assume there are less than 100 adults in the group
        if i > 25:  # There are 25 more adults than children
            num_adults = i
            num_children = i - 25
            if (num_adults * adult_price) + (num_children * child_price) == total_price:  # Check if the total price matches
                break

    result = num_children
    return result

print(solution())