def solution():
    """Mr. Zubir bought a pair of pants, a shirt, and a coat. The pair of pants and shirt costs $100. The pants and coat cost $244. The coat costs 5 times as much as the shirt. How much did Mr. Zubir pay for his coat?"""
    # Define the total cost of the pants and shirt
    pants_shirt_cost = 100

    # Define the total cost of the pants and coat
    pants_coat_cost = 244

    # Solve the system of equations to find the cost of the coat
    # p + s = 100
    # p + c = 244
    # c = 5s
    # By substitution, p = 100 - s and c = 5s
    # Substituting in the second equation, (100 - s) + c = 244
    # c = 144 + s
    # Substituting in the third equation, 5s = 144 + s
    # s = 36 and c = 180

    coat_cost = 180

    # return the result
    result = coat_cost
    return result

print(solution())