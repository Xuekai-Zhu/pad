def solution():
    """Mr. Shaefer harvested 500 lychees in a carton and took them to the market. He sold half of them and took home the remaining number of lychees where they ate 3/5 of them. Calculate the number of lychees remaining."""
    lychees_in_carton = 500
    sold_lychees = lychees_in_carton / 2
    remaining_lychees = lychees_in_carton - sold_lychees
    eaten_lychees = remaining_lychees * (3/5)
    lychees_remaining = remaining_lychees - eaten_lychees
    result = lychees_remaining
    return result

print(solution())