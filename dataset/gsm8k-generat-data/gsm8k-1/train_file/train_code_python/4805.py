def solution():
    """Melissa is repairing her shoes. For each shoe, it takes her 5 minutes to replace the buckle and 10 minutes to even out the heel. How many minutes does Melissa spend on this project total?"""
    time_per_shoe = 5 + 10
    shoes_to_repair = 2  # assuming she is repairing a pair of shoes
    total_time = time_per_shoe * shoes_to_repair
    result = total_time
    return result

print(solution())