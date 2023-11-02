def solution():
    """John buys 3 boxes of burritos.  He gives away a 3rd of them to his friend.  Each box has 20 burritos.  He eats 3 burritos per day for 10 days.  How many burritos does he have left?"""
    # Define the number of boxes of burritos and burritos per box
    BOXES = 3
    BURRITOS_PER_BOX = 20

    # Calculate the total number of burritos
    total_burritos = BOXES * BURRITOS_PER_BOX

    # Give away a third of the burritos
    given_away = total_burritos // 3
    remaining_burritos = total_burritos - given_away

    # Calculate the number of burritos John eats
    eaten = 3 * 10

    # Calculate the number of burritos John has left
    remaining_burritos -= eaten

    # Display the number of burritos John has left
    result = remaining_burritos
    return result

print(solution())