def solution():
    """Each of the three Morales sisters owns an orange grove that has 110 trees. Each orange tree produces medium-sized oranges. At harvest time, Gabriela's grove produced 600 oranges per tree, while Alba harvested 400 per tree. Each of Maricela's trees produced 500 oranges. With such a huge harvest, the sisters are thinking of making orange juice for sale. If it takes three medium-sized oranges to make 1 cup of juice, and then they sell each cup for $4, how much money will they make?"""
    # Define the number of trees and oranges per tree owned by each sister
    TREE_COUNT = 110
    GABRIELA_ORANGES = 600
    ALBA_ORANGES = 400
    MARICELA_ORANGES = 500

    # Calculate the total number of oranges harvested by each sister's grove
    gabriela_total_oranges = GABRIELA_ORANGES * TREE_COUNT
    alba_total_oranges = ALBA_ORANGES * TREE_COUNT
    maricela_total_oranges = MARICELA_ORANGES * TREE_COUNT

    # Calculate the total number of oranges harvested by all three sisters
    total_oranges = gabriela_total_oranges + alba_total_oranges + maricela_total_oranges

    # Calculate the total number of cups of juice that can be made from the oranges
    total_cups = total_oranges // 3

    # Calculate the total amount of money the sisters can make selling the juice
    total_money = total_cups * 4

    # Display the total money made
    result = total_money
    return result

print(solution())