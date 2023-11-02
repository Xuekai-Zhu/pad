def solution():
    """Alex was having a cookout Friday night and planned to serve burgers to his guests.  He planned to cook 3 burgers for each guest and had invited 10 friends over.  1 of his friends didn't eat meat and said they would bring their own food.  Another one of his friends didn't eat bread and would not need the buns.  The burger buns came 8 to a pack.  How many packs of buns did Alex need to buy?"""
    # Calculate the total number of burgers needed (including friend who brings their own food)
    total_burgers = (10 + 1) * 3

    # Calculate the total number of buns needed (assuming each burger requires one bun)
    total_buns = total_burgers

    # Subtract the number of buns not needed (from the friend who doesn't eat bread)
    total_buns -= 3

    # Calculate the number of packs of buns needed
    packs_of_buns = total_buns // 8
    if total_buns % 8 != 0:
        packs_of_buns += 1

    # Display the number of packs of buns needed
    result = packs_of_buns
    return result

print(solution())