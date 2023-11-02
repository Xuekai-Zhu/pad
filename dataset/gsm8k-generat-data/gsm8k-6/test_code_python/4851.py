def solution():
    # Calculate the total number of silverware pieces Stephanie needs to purchase
    spoons = (5 + 10 - 4) * 1  # 5 for herself plus 10 extra with 4 fewer, multiplied by 1 type
    butter_knives = (5 + 10 - 4) * 1
    steak_knives = (5 + 10 - 5 - 4) * 1  # 5 for herself plus 10 extra with 5 fewer, 4 fewer, multiplied by 1 type
    forks = (5 + 10 - 3 - 4) * 1  # 5 for herself plus 10 extra with 3 fewer, 4 fewer, multiplied by 1 type
    total_silverware = spoons + butter_knives + steak_knives + forks  # total number of silverware pieces
    result = total_silverware
    return result

print(solution())