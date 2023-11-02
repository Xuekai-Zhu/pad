def solution():
    """An elementary school teacher is making Halloween goodie bags for her class. She wants the bags to be personalized, so she surveys her students asking whether they'd like a vampire-themed bag or a pumpkin-themed bag. Of her 25 students, 11 indicate they want the vampire-themed bag and 14 indicate they want the pumpkin-themed bag. The store the teacher shops at sells packs of 5 of each theme at a price of $3 per package, as well as individual bags of each theme at a price of $1 each. What is the least amount of money the teacher can spend on the bags if she buys every student the theme they requested?"""
    num_students = 25
    num_vampire_bags = 11
    num_pumpkin_bags = 14
    bags_per_pack = 5
    pack_price = 3
    individual_price = 1
    
    # calculate number of packs needed for each theme
    num_vampire_packs = (num_vampire_bags - 1) // bags_per_pack + 1
    num_pumpkin_packs = (num_pumpkin_bags - 1) // bags_per_pack + 1
    
    # calculate total cost of packs
    pack_cost = num_vampire_packs * pack_price + num_pumpkin_packs * pack_price
    
    # calculate number of individual bags needed for each theme
    num_vampire_individual = num_vampire_bags % bags_per_pack
    num_pumpkin_individual = num_pumpkin_bags % bags_per_pack
    
    # calculate total cost of individual bags
    individual_cost = num_vampire_individual * individual_price + num_pumpkin_individual * individual_price
    
    # calculate total cost
    total_cost = pack_cost + individual_cost
    
    result = total_cost
    return result

print(solution())