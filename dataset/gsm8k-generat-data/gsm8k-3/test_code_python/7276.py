def solution():
    """The bowl of fruit contains apples, pears, and bananas. There are two more pears than apples, and three more bananas than pears. If the bowl contains 19 pieces of fruit, how many bananas does it contain?"""
    # Define the number of apples and use it to find the number of pears and bananas
    apples = x
    pears = apples + 2
    bananas = pears + 3

    # Use the total number of fruit to set up an equation
    total_fruit = 19
    equation = apples + pears + bananas == total_fruit

    # Solve for bananas
    bananas = solve(equation, bananas)

    result = bananas[0]
    return result

print(solution())