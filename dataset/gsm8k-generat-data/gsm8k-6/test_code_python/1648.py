def solution():
    # Calculate the total jumping jacks done so far this week
    total_jumping_jacks = 34 + 20 + 0 + 123 + 64 + 23  # Kenny skipped Tuesday
    # Calculate the number of jumping jacks he needs to do on Saturday to beat last week's number
    jumping_jacks_needed = 325 - total_jumping_jacks  # Kenny wants to do more than last week's 324 jumping jacks
    result = jumping_jacks_needed
    return result

print(solution())