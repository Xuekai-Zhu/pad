def solution():
    berries_per_day = 1/2  # Martin eats 1/2 cup of berries every day
    berries_per_pack = 1  # The grocery store package contains 1 cup of berries
    cost_per_pack = 2.00  # The grocery store sells the package of berries for $2.00
    number_of_days = 30  # Martin wants to know how much he will spend on berries in a 30 day period

    # Calculate the total number of cups of berries Martin will need in 30 days
    total_berrie_cups = berries_per_day * number_of_days

    # Calculate the total number of berry packs Martin will need
    total_berrie_packs = total_berrie_cups / berries_per_pack

    # Calculate the total cost of the berry packs
    total_cost = total_berrie_packs * cost_per_pack
    result = total_cost
    return result

print(solution())