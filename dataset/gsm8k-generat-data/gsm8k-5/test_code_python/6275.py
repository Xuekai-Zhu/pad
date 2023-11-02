def solution():
    required_length = 10 * 6 / 12  # Tanesha needs 10 pieces of rope each 6 inches long, which is equivalent to 10 * 6 / 12 feet
    option1_cost = 5  # 6-foot length of rope that costs $5
    option2_cost = (required_length // 1) * 1.25 + ((required_length % 1) * 1.25)  # Cost of buying 1-foot lengths of rope to get the required length

    # Determine the least cost option
    if option1_cost <= option2_cost:
        result = option1_cost
    else:
        result = option2_cost
    return result

print(solution())