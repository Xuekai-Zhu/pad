def solution():
    # Calculate the total weight of potato chips needed for the party
    total_weight = 1.2 * 10  # 10 people at the party and each person will get 1.2 pounds

    # Calculate the total cost of potato chips
    cost = 0.25 * total_weight  # potato chips cost 25 cents per pound
    cost_in_dollars = cost / 100  # convert cents to dollars

    result = cost_in_dollars
    return result

print(solution())