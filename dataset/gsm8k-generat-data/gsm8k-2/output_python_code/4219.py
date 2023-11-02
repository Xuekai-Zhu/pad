def solution():
    """A warehouse store sells cartons of gum. Each carton contains 5 packs of gum, and there are 3 sticks of gum in each pack. Each brown box contains 4 cartons of gum. How many sticks of gum are there in 8 brown boxes?"""
    sticks_per_pack = 3
    packs_per_carton = 5
    cartons_per_box = 4
    boxes = 8
    sticks_per_carton = sticks_per_pack * packs_per_carton
    sticks_per_box = sticks_per_carton * cartons_per_box
    total_sticks = sticks_per_box * boxes
    result = total_sticks
    return result

print(solution())