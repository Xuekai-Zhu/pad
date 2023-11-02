def solution():
    # Calculate the total cost for 6 friends to eat 2 bars each
    total_bars = 6 * 2  # 6 friends eat 2 bars each
    total_cost = (total_bars / 3) * 7.5  # a box contains 3 bars and costs $7.50
    cost_per_person = total_cost / 6  # divide the total cost by the number of friends
    result = cost_per_person
    return result

print(solution())