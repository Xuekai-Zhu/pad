def solution():
    """Mrs. Lacson harvested 80 sweet potatoes. She sold 20 of them to Mrs. Adams and 15 of them to Mr. Lenon. How many sweet potatoes are not yet sold?"""
    total_harvested = 80
    sold_to_adams = 20
    sold_to_lenon = 15
    remaining_potatoes = total_harvested - sold_to_adams - sold_to_lenon
    result = remaining_potatoes
    return result

print(solution())