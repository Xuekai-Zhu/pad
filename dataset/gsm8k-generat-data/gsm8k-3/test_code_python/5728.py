def solution():
    """The cost of a slice of cake is three-fourths of the cost of a cup of milk tea. If the milk tea costs $2.40, how much do 2 slices of cake and 1 cup of milk tea cost?"""
    # Define the cost of a cup of milk tea
    milk_tea_cost = 2.4

    # Define the cost of a slice of cake in terms of the cost of a cup of milk tea
    cake_cost = 0.75 * milk_tea_cost

    # Calculate the cost of 2 slices of cake and 1 cup of milk tea
    total_cost = (2 * cake_cost) + milk_tea_cost

    # Display the total cost
    result = total_cost
    return result

print(solution())