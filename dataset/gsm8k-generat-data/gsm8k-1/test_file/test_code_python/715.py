def solution():
    """Goldy bought 20 sacks of rice and gave 3 sacks to her cousin and 4 sacks to her brother, if there are 25 kilograms of rice per sack, how many kilograms does she gave to her cousin and brother?"""
    sacks_bought = 20
    sacks_given_cousin = 3
    sacks_given_brother = 4
    sacks_remaining = sacks_bought - sacks_given_cousin - sacks_given_brother
    kg_per_sack = 25
    kg_given_cousin = sacks_given_cousin * kg_per_sack
    kg_given_brother = sacks_given_brother * kg_per_sack
    total_kg_given = kg_given_cousin + kg_given_brother
    result = total_kg_given
    return result

print(solution())