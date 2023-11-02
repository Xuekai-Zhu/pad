def solution():
    # Calculate the total amount Rita spent
    dresses_cost = 5 * 20  # 5 short dresses cost $20 each
    pants_cost = 3 * 12  # 3 pairs of pants cost $12 each
    jackets_cost = 4 * 30  # 4 jackets cost $30 each
    total_cost = dresses_cost + pants_cost + jackets_cost + 5  # Rita spent an additional $5 on transportation

    # Calculate how much Rita has left
    initial_money = 400
    remaining_money = initial_money - total_cost
    result = remaining_money
    return result

print(solution())