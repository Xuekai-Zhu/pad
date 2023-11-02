def solution():
    """Each of the three Morales sisters owns an orange grove that has 110 trees. Each orange tree produces medium-sized oranges.
    At harvest time, Gabriela's grove produced 600 oranges per tree, while Alba harvested 400 per tree. Each of Maricela's trees produced 500 oranges.
    With such a huge harvest, the sisters are thinking of making orange juice for sale. If it takes three medium-sized oranges to make 1 cup
    of juice, and then they sell each cup for $4, how much money will they make?"""
    # Define the number of orange trees in each grove
    tree_count = 110
    gabriela_trees = tree_count
    alba_trees = tree_count
    maricela_trees = tree_count

    # Calculate the number of oranges produced by each grove
    gabriela_oranges = gabriela_trees * 600
    alba_oranges = alba_trees * 400
    maricela_oranges = maricela_trees * 500

    # Calculate the total number of oranges among the three groves
    total_oranges = gabriela_oranges + alba_oranges + maricela_oranges

    # Calculate the number of cups of orange juice that can be made
    cups_of_juice = total_oranges // 3

    # Calculate the total revenue from selling the orange juice
    total_revenue = cups_of_juice * 4

    # return the result
    result = total_revenue
    return result

print(solution())