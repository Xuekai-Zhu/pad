def solution():
    # Calculate the number of CDs sold at $10 and $5 each
    num_cd_10 = 0.4 * 200
    num_cd_5 = 0.6 * 200

    # Calculate the number of CDs Prince bought at $10 each
    num_cd_10_prince = 0.5 * num_cd_10

    # Calculate the total cost spent by Prince
    total_cost = num_cd_10_prince * 10 + num_cd_5 * 5
    result = total_cost
    return result

print(solution())