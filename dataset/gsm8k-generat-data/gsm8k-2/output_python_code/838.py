def solution():
    """The Rotary Club is holding its annual fundraising Omelet Breakfast, with tickets sold in advance. The tickets come in different price levels, for young children, older children, adults, and seniors. This year they sold 53 small children tickets, 35 older children tickets, 75 adult tickets, and 37 senior tickets. To figure out how many eggs they need to buy, the club estimates that small children can eat a half omelet, older children can eat a whole omelet, adults will eat two omelets, and seniors will eat one and a half omelets. Just to be on the safe side, they get enough eggs to make 25 extra omelets. If they use 2 eggs for each omelet, how many eggs will they need to buy?"""
    small_children = 53
    older_children = 35
    adults = 75
    seniors = 37

    eggs_per_half_omelet = 1
    eggs_per_whole_omelet = 2
    eggs_per_one_and_half_omelets = 3

    total_omelets = (small_children * 0.5) + (older_children * 1) + (adults * 2) + (seniors * 1.5) + 25

    total_eggs = 2 * (total_omelets)

    result = total_eggs
    return result

print(solution())