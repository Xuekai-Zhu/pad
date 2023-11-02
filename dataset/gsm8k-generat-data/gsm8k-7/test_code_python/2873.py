def solution():
    num_children = 40
    num_toddlers = 6
    num_teenagers = num_toddlers * 5

    # Calculate the total number of teenagers and toddlers combined
    total_teenagers_and_toddlers = num_teenagers + num_toddlers

    # Calculate the number of newborns
    num_newborns = num_children - total_teenagers_and_toddlers
    result = num_newborns
    return result

print(solution())