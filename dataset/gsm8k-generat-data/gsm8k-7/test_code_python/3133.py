def solution():
    num_trees_per_grove = 110

    # Calculate the total number of oranges harvested from Gabriela's grove
    gabriela_oranges = 600 * num_trees_per_grove

    # Calculate the total number of oranges harvested from Alba's grove
    alba_oranges = 400 * num_trees_per_grove

    # Calculate the total number of oranges harvested from Maricela's grove
    maricela_oranges = 500 * num_trees_per_grove

    # Calculate the total number of oranges harvested from all three groves
    total_oranges = gabriela_oranges + alba_oranges + maricela_oranges

    # Calculate the total number of cups of juice they can make
    total_juice = total_oranges / 3

    # Calculate the total revenue from selling the juice
    total_revenue = total_juice * 4
    result = total_revenue
    return result

print(solution())