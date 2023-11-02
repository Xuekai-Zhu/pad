def solution():
    """Jack and Jill shared the cost of renting a cottage that costs $5 an hour. If they rented it for eight hours, how much did each friend pay?"""
    renting_cost_per_hour = 5
    hours_rented = 8
    total_renting_cost = renting_cost_per_hour * hours_rented
    cost_per_friend = total_renting_cost / 2
    result = cost_per_friend
    return result

print(solution())