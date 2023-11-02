def solution():
    """Tina made a large pan of brownies and cut it into 24 pieces. She had one with lunch and dinner every day for 5 days. Her husband snagged one per day for 5 days to take to work. They shared 4 with dinner guests. How many brownies were left?"""
    total_brownies = 24
    eaten_by_tina = 2 * 5
    eaten_by_husband = 5
    shared_with_guests = 4
    total_eaten = eaten_by_tina + eaten_by_husband + shared_with_guests
    brownies_left = total_brownies - total_eaten
    result = brownies_left
    return result

print(solution())