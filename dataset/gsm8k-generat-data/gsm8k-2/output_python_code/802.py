def solution():
    """An elementary school teacher is making Halloween goodie bags for her class. She wants the bags to be personalized, so she surveys her students asking whether they'd like a vampire-themed bag or a pumpkin-themed bag. Of her 25 students, 11 indicate they want the vampire-themed bag and 14 indicate they want the pumpkin-themed bag. The store the teacher shops at sells packs of 5 of each theme at a price of $3 per package, as well as individual bags of each theme at a price of $1 each. What is the least amount of money the teacher can spend on the bags if she buys every student the theme they requested?"""
    vampire_students = 11
    pumpkin_students = 14
    vampire_pack_price = 3
    pumpkin_pack_price = 3
    individual_bag_price = 1
    vampire_packs = vampire_students // 5
    if vampire_students % 5 != 0:
        vampire_packs += 1
    pumpkin_packs = pumpkin_students // 5
    if pumpkin_students % 5 != 0:
        pumpkin_packs += 1
    vampire_pack_cost = vampire_packs * vampire_pack_price
    pumpkin_pack_cost = pumpkin_packs * pumpkin_pack_price
    vampire_individual_cost = (vampire_students % 5) * individual_bag_price
    pumpkin_individual_cost = (pumpkin_students % 5) * individual_bag_price
    total_cost = vampire_pack_cost + pumpkin_pack_cost + vampire_individual_cost + pumpkin_individual_cost
    result = total_cost
    return result

print(solution())