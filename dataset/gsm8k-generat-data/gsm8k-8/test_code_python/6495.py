def solution():
    # Calculate the number of days Bart will burn firewood
    # November has 30 days, December has 31 days, January has 31 days, and February has 28 days
    num_days = 30 + 31 + 31 + 28
    # Calculate the number of logs Bart will burn during this time
    num_logs = 5 * num_days
    # Calculate the number of trees Bart needs to cut down to obtain this many logs
    num_trees = num_logs / 75
    result = num_trees
    return result

print(solution())