def solution():
    """James hires a seamstress to fix all his shirts and pants. He has 10 shirts and 12 pairs of pants. It takes 1.5 hours to fix a shirt and twice as long for pants. The tailor charges $30 per hour. How much does it cost?"""
    num_shirts = 10
    num_pants = 12
    shirt_time = 1.5
    pant_time = 2 * shirt_time
    hourly_rate = 30
    total_time = num_shirts * shirt_time + num_pants * pant_time
    total_cost = total_time * hourly_rate
    result = total_cost
    return result

print(solution())