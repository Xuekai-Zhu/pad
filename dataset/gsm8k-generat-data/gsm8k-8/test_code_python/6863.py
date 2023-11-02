def solution():
    #Calculate the number of logs produced for each tree
    logs_per_tree = 4

    #Calculate the total number of logs produced
    total_logs = 500 / 5

    #Calculate the number of trees chopped down
    trees_chopped = total_logs / logs_per_tree
    result = trees_chopped
    return result

print(solution())