def solution():
    """The cost of a slice of cake is three-fourths of the cost of a cup of milk tea. If the milk tea costs $2.40, how much do 2 slices of cake and 1 cup of milk tea cost?"""
    milk_tea_cost = 2.40
    cake_cost = 0.75 * milk_tea_cost
    total_cost = (2 * cake_cost) + milk_tea_cost
    result = total_cost
    return result

print(solution())