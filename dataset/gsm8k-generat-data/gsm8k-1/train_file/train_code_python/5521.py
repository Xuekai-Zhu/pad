def solution():
    """Mrs. Lacson harvested 80 sweet potatoes. She sold 20 of them to Mrs. Adams and 15 of them to Mr. Lenon. How many sweet potatoes are not yet sold?"""
    total_potatoes = 80
    sold_potatoes = 20 + 15
    remaining_potatoes = total_potatoes - sold_potatoes
    result = remaining_potatoes
    return result

print(solution())