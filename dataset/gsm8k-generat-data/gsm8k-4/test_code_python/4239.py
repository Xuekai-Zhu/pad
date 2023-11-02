def solution():
    """Alex was having a cookout Friday night and planned to serve burgers to his guests. He planned to cook 3 burgers for each guest and had invited 10 friends over. 1 of his friends didn't eat meat and said they would bring their own food. Another one of his friends didn't eat bread and would not need the buns. The burger buns came 8 to a pack. How many packs of buns did Alex need to buy?"""
    # Define the number of guests
    guests = 10

    # Calculate the number of burgers needed
    burgers = guests * 3

    # Adjust for the friend who brings their own food
    burgers -= 3

    # Adjust for the friend who doesn't eat bread
    buns = burgers + 10
    buns -= burgers // 3

    # Calculate the number of packs of buns needed
    packs_of_buns = buns // 8 + (buns % 8 > 0)

    result = packs_of_buns
    return result

print(solution())