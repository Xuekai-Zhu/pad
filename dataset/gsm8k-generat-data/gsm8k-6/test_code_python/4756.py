def solution():
    # Calculate the temperature drop
    temp_drop = 80 - 78.2  # temperature drops from 80 to 78.2 degrees after planting trees
    # Calculate the number of trees needed to achieve the temperature drop
    trees_needed = int(temp_drop / 0.1)  # for each tree planted, the temperature drops .1 degree

    # Calculate the total cost of planting the trees
    total_cost = trees_needed * 6  # a tree costs $6 to plant

    result = total_cost
    return result

print(solution())