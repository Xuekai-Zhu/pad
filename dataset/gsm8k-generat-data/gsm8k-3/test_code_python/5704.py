def solution():
    """The total cost of Olivia’s groceries was $42. The bananas cost her $12, the bread cost her $9, and the milk cost her $7. The only other groceries she bought were apples. In dollars, how much money did the apples cost her?"""
    # Define the cost of each grocery item
    BANANA_COST = 12
    BREAD_COST = 9
    MILK_COST = 7

    # Calculate the total cost of the groceries
    total_cost = 42

    # Calculate the cost of the apples
    apple_cost = total_cost - BANANA_COST - BREAD_COST - MILK_COST

    # Display the cost of the apples
    result = apple_cost
    return result

print(solution())