def solution():
    """Mr. Smith has two farms, Farm X and Farm Y. He has 55 goats in Farm X and 45 goats in Farm Y. He sold 10 goats from Farm X and twice as many goats from Farm Y. How many goats are left in the two farms altogether?"""
    goats_X = 55
    goats_Y = 45
    sold_X = 10
    sold_Y = 2 * sold_X
    remaining_X = goats_X - sold_X
    remaining_Y = goats_Y - sold_Y
    total_remaining = remaining_X + remaining_Y
    result = total_remaining
    return result

Solution: 
def solution():
    """Samantha's last name has three fewer letters than Bobbie's last name. If Bobbie took two letters off her last name, she would have a last name twice the length of Jamie's. Jamie's full name is Jamie Grey. How many letters are in Samantha's last name?"""
    jamie_last_name = 'Grey'
    bobbi_last_name = (len(jamie_last_name) * 2) + 2
    samantha_last_name = bobbi_last_name - 3
    result = samantha_last_name
    return result

print(solution())