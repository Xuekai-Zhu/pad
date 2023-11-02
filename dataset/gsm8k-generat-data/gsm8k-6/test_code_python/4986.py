def solution():
    # Calculate the total cost of ingredients
    flour_cost = 2 * 4  # 2 cups of flour at $4 per cup
    sugar_cost = 2 * 2  # 2 cups of sugar at $2 per cup
    egg_cost = 2 * 0.5  # 2 eggs at $0.5 per egg
    butter_cost = 1 * 2.5  # 1 cup of butter at $2.5 per cup
    total_cost = flour_cost + sugar_cost + egg_cost + butter_cost

    # Calculate the cost of one slice of cake
    cost_per_slice = total_cost / 6

    # Calculate the cost of the cake that was eaten by the mother
    cost_eaten = 2 * cost_per_slice

    # Calculate the cost of the cake eaten by the dog
    cost_dog = (6 - 2) * cost_per_slice

    result = cost_dog
    return result

print(solution())