def solution():
    """Jamie and Oliver are planning to go on a vacation. A plane ticket costs $24 for each person and a hotel stay costs $12 for each person per day. How much money will they spend on the vacation if they stay for 3 days?"""
    num_people = 2
    ticket_cost = 24 * num_people
    hotel_cost = 12 * num_people * 3
    total_cost = ticket_cost + hotel_cost
    result = total_cost
    return result

print(solution())