def solution():
    """Tina made a large pan of brownies and cut it into 24 pieces. She had one with lunch and dinner every day for 5 days. Her husband snagged one per day for 5 days to take to work. They shared 4 with dinner guests. How many brownies were left?"""
    total_brownies = 24
    brownies_per_day = 2
    days = 5
    brownies_eaten_by_tina = brownies_per_day * days
    brownies_eaten_by_husband = brownies_per_day * days
    brownies_shared_with_guests = 4
    total_brownies_eaten = (brownies_eaten_by_tina + brownies_eaten_by_husband + brownies_shared_with_guests)
    brownies_left = total_brownies - total_brownies_eaten
    result = brownies_left
    return result

print(solution())