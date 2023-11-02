def solution():
    # Calculate the number of slices of cheese used for ham sandwiches
    ham_cheese = 2 * 10

    # Calculate the remaining number of slices of cheese available for grilled cheese sandwiches
    remaining_cheese = 50 - ham_cheese

    # Calculate the number of grilled cheese sandwiches that can be made
    grilled_cheese = remaining_cheese // 3

    result = grilled_cheese
    return result

print(solution())