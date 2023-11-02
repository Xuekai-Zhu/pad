def solution():
    # Calculate the number of logs needed for 500 pieces of firewood
    logs_needed = 500/5  # each log produces 5 pieces of firewood

    # Calculate the number of trees needed to produce the necessary number of logs
    trees_needed = logs_needed/4  # each tree produces 4 logs

    result = trees_needed
    return result

print(solution())