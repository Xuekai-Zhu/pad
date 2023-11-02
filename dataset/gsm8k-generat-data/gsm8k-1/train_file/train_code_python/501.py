def solution():
    """At a garage sale, Tish bought 4 items: a red horseshoe magnet, two stuffed animals, and a large sticker which read, "Why can't teachers solve their own math problems?" The magnet cost three times more than the sticker, but only one quarter the price of the two stuffed animals combined. If the Magnet cost $3, how much, in dollars, did a single stuffed animal cost?"""
    magnet_price = 3
    sticker_price = magnet_price / 3
    combined_stuffed_animals_price = magnet_price * 4
    single_stuffed_animal_price = (combined_stuffed_animals_price - magnet_price) / 2
    result = single_stuffed_animal_price
    
    return result

print(solution())