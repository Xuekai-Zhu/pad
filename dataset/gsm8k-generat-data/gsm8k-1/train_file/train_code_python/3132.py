def solution():
    """Each of the three Morales sisters owns an orange grove that has 110 trees. Each orange tree produces medium-sized oranges. At harvest time, Gabriela's grove produced 600 oranges per tree, while Alba harvested 400 per tree. Each of Maricela's trees produced 500 oranges. With such a huge harvest, the sisters are thinking of making orange juice for sale. If it takes three medium-sized oranges to make 1 cup of juice, and then they sell each cup for $4, how much money will they make?"""
    num_trees = 110
    gabriela_oranges = 600
    alba_oranges = 400
    maricela_oranges = 500
    total_oranges = num_trees * (gabriela_oranges + alba_oranges + maricela_oranges)
    cups_of_juice = total_oranges / 3
    price_per_cup = 4
    revenue = cups_of_juice * price_per_cup
    result = revenue
    return result

print(solution())