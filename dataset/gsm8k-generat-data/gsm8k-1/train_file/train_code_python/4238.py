def solution():
    """Alex was having a cookout Friday night and planned to serve burgers to his guests. He planned to cook 3 burgers for each guest and had invited 10 friends over. 1 of his friends didn't eat meat and said they would bring their own food. Another one of his friends didn't eat bread and would not need the buns. The burger buns came 8 to a pack. How many packs of buns did Alex need to buy?"""
    guests = 10
    burgers_per_guest = 3
    buns_per_pack = 8
    buns_needed = (guests * burgers_per_guest) / 3 * 4
    packs_needed = buns_needed / buns_per_pack
    result = math.ceil(packs_needed)
    return result

print(solution())