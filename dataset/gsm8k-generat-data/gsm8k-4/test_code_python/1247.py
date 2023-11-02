def solution():
    """The number of cards in a card game was 500. Two friends Ellis and Orion, playing together, divided the cards in the ratio of 11:9. How many more cards did Ellis get than Orion?"""
    # Define the total number of cards and the ratio of division
    total_cards = 500
    ratio = 11/9

    # Calculate the total number of parts in the ratio
    total_parts = 11 + 9

    # Calculate the number of parts that Ellis should get
    ellis_parts = ratio / total_parts * total_cards

    # Calculate the number of parts that Orion should get
    orion_parts = (1 - ratio) / total_parts * total_cards

    # Calculate the difference in the number of cards that Ellis and Orion got
    difference = ellis_parts - orion_parts

    # Round the difference to the nearest integer
    result = round(difference)
    return result

print(solution())