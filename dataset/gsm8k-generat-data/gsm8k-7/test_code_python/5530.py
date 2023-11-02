def solution():
    num_own_blueberries = 100
    num_neighbor_blueberries = 200
    num_blueberries_per_pie = 100

    # Calculate the total number of blueberries Simon has
    total_blueberries = num_own_blueberries + num_neighbor_blueberries

    # Calculate the number of pies Simon can make
    num_pies = total_blueberries // num_blueberries_per_pie
    result = num_pies
    return result

print(solution())