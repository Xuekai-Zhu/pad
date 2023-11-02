def solution():
    milk_tea_cost = 2.4

    # Calculate the cost of one slice of cake
    cake_cost = 3/4 * milk_tea_cost

    # Calculate the cost of 2 slices of cake
    total_cake_cost = 2 * cake_cost

    # Calculate the total cost of 2 slices of cake and 1 cup of milk tea
    total_cost = total_cake_cost + milk_tea_cost

    result = total_cost
    return result

print(solution())