def solution():
    """John buys 3 boxes of burritos. He gives away a 3rd of them to his friend. Each box has 20 burritos. He eats 3 burritos per day for 10 days. How many burritos does he have left?"""
    # Define the number of boxes and burritos per box
    num_boxes = 3
    burritos_per_box = 20

    # Calculate the total number of burritos
    total_burritos = num_boxes * burritos_per_box

    # Give away a third of the burritos to John's friend
    friend_burritos = total_burritos / 3

    # Calculate the number of burritos John has left
    john_burritos = total_burritos - friend_burritos

    # Calculate the number of burritos John eats in 10 days
    john_eats = 3 * 10

    # Calculate the number of burritos John has left
    john_left = john_burritos - john_eats

    result = john_left
    return result

print(solution())