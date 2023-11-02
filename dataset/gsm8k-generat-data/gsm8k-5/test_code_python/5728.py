def solution():
    milk_tea_cost = 2.40  # Cost of a cup of milk tea
    cake_cost = 0.75 * milk_tea_cost  # Cost of a slice of cake

    # Calculate the total cost of 2 slices of cake and 1 cup of milk tea
    total_cost = (2 * cake_cost) + milk_tea_cost
    result = total_cost
    return result

print(solution())