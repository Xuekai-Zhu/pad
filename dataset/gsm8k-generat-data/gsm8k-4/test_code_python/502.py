def solution():
    """At a garage sale, Tish bought 4 items: a red horseshoe magnet, two stuffed animals, and a large sticker which read, "Why can't teachers solve their own math problems?" The magnet cost three times more than the sticker, but only one quarter the price of the two stuffed animals combined. If the Magnet cost $3, how much, in dollars, did a single stuffed animal cost?"""
    
    # Define the cost of the magnet and the relationship with other items
    magnet_cost = 3
    sticker_cost = magnet_cost/3
    stuffed_animals_cost = 4*magnet_cost

    # Calculate the total cost of the four items
    total_cost = magnet_cost + 2*stuffed_animals_cost + sticker_cost

    # Calculate the cost of a single stuffed animal
    single_stuffed_animal_cost = (total_cost - magnet_cost - 2*sticker_cost)/2

    result = single_stuffed_animal_cost
    return result

print(solution())