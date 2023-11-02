def solution():
    """The bakers at the Beverly Hills Bakery baked 200 loaves of bread on Monday morning. They sold 93 loaves in the morning and 39 loaves in the afternoon. A grocery store returned 6 unsold loaves. How many loaves of bread did they have left?"""
    total_baked = 200
    sold_in_morning = 93
    sold_in_afternoon = 39
    returned = 6
    remaining = total_baked - sold_in_morning - sold_in_afternoon + returned
    result = remaining
    return result

print(solution())