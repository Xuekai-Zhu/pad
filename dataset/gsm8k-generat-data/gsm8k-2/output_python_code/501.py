def solution():
    """At a garage sale, Tish bought 4 items: a red horseshoe magnet, two stuffed animals, and a large sticker which read, "Why can't teachers solve their own math problems?" The magnet cost three times more than the sticker, but only one quarter the price of the two stuffed animals combined. If the Magnet cost $3, how much, in dollars, did a single stuffed animal cost?"""
    magnet_cost = 3
    sticker_cost = magnet_cost / 3
    combined_stuffed_animal_cost = magnet_cost * 4
    single_stuffed_animal_cost = (combined_stuffed_animal_cost - magnet_cost) / 2
    result = single_stuffed_animal_cost
    return result

print(solution())