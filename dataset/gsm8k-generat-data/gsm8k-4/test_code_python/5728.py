def solution():
    """The cost of a slice of cake is three-fourths of the cost of a cup of milk tea. If the milk tea costs $2.40, how much do 2 slices of cake and 1 cup of milk tea cost?"""
    # Define the cost of milk tea
    milk_tea_cost = 2.4

    # Calculate the cost of a slice of cake
    cake_cost = milk_tea_cost * 0.75

    # Calculate the total cost of 2 slices of cake and 1 cup of milk tea
    total_cost = (2 * cake_cost) + milk_tea_cost

    result = round(total_cost, 2)
    return result

print(solution())