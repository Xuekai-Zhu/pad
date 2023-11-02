def solution():
    num_students = 25
    num_vampire_bags = 11
    num_pumpkin_bags = 14
    bags_per_pack = 5
    pack_price = 3
    individual_price = 1

    # Calculate the number of packs of each theme the teacher will need to buy
    num_vampire_packs = num_vampire_bags // bags_per_pack + (1 if num_vampire_bags % bags_per_pack != 0 else 0)
    num_pumpkin_packs = num_pumpkin_bags // bags_per_pack + (1 if num_pumpkin_bags % bags_per_pack != 0 else 0)

    # Calculate the total cost of buying packs of each theme
    total_pack_cost = num_vampire_packs * pack_price + num_pumpkin_packs * pack_price

    # Calculate the number of individual bags of each theme the teacher will need to buy
    num_vampire_individual = num_vampire_bags % bags_per_pack
    num_pumpkin_individual = num_pumpkin_bags % bags_per_pack

    # Calculate the total cost of buying individual bags of each theme
    total_individual_cost = num_vampire_individual * individual_price + num_pumpkin_individual * individual_price

    # Calculate the total cost for all bags
    total_cost = total_pack_cost + total_individual_cost
    result = total_cost
    return result

print(solution())