def solution():
    # Calculate the total number of frogs
    total_frogs = 5 + 2 + 2 + 18  

    # Calculate the total number of mutated frogs
    mutated_frogs = 5 + 2 + 2  

    # Calculate the percentage of frogs that have mutated
    percentage_mutated = round((mutated_frogs / total_frogs) * 100)

    result = percentage_mutated
    return result

print(solution())