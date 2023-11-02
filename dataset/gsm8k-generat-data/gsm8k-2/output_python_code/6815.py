def solution():
    """Every morning Harry takes 15 minutes to buy coffee and a bagel and twice that long to read the paper and eat before going in to work. How long does Harry's morning routine take?"""
    coffee_bagel_time = 15
    paper_eat_time = 2 * coffee_bagel_time
    total_time = coffee_bagel_time + paper_eat_time
    result = total_time
    return result

print(solution())