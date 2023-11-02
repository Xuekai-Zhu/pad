def solution():
    """Twice Betty's age is the cost of a pack of nuts. Doug, Betty's friend, is 40 years old. If the sum of their ages is 90, and Betty wants to buy 20 packs of the nuts, calculate the amount of money she'll pay for the packs of nuts."""
    doug_age = 40
    total_age = 90
    betty_age = total_age - doug_age
    nut_cost = 2 * betty_age
    num_packs = 20
    total_cost = nut_cost * num_packs
    result = total_cost
    return result

print(solution())