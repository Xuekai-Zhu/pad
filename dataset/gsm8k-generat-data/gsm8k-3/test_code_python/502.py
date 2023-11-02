def solution():
    """At a garage sale, Tish bought 4 items: a red horseshoe magnet, two stuffed animals, and a large sticker which read, "Why can't teachers solve their own math problems?"  The magnet cost three times more than the sticker, but only one quarter the price of the two stuffed animals combined.  If the Magnet cost $3, how much, in dollars, did a single stuffed animal cost?"""
    # Define the cost of the magnet
    magnet_cost = 3

    # Define the cost ratio between the magnet and the sticker
    magnet_sticker_ratio = 3

    # Define the ratio between the magnet and the combined cost of the two stuffed animals
    magnet_stuffed_ratio = 1/4

    # Calculate the cost of the sticker
    sticker_cost = magnet_cost / magnet_sticker_ratio

    # Calculate the combined cost of the two stuffed animals
    stuffed_cost = magnet_cost / magnet_stuffed_ratio

    # Calculate the cost of a single stuffed animal
    single_stuffed_cost = (stuffed_cost - magnet_cost) / 2

    # Display the cost of a single stuffed animal
    result = single_stuffed_cost
    return result

print(solution())