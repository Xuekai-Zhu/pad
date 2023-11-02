def solution():
    """Daryl is loading crates at a warehouse and wants to make sure that they are not overloaded. Each crate can weigh up to 20kg and he has 15 crates he can fill. He has 4 bags of nails to load, each of which weighs 5kg; he has 12 bags of hammers, each of which weighs 5 kg; he also has 10 bags of wooden planks, each of which weighs 30kg and can be sub-divided. He realizes that he has too much to load and will have to leave some items out of the crates to meet the weight limit. In kg, how much is Daryl going to have to leave out of the crates?"""
    crate_weight_limit = 20
    num_crates = 15
    nails_weight = 5
    hammers_weight = 5
    planks_weight = 30
    num_nails = 4
    num_hammers = 12
    num_planks = 10
    
    total_weight = (nails_weight * num_nails) + (hammers_weight * num_hammers) + (planks_weight * num_planks)
    weight_left_out = total_weight - (crate_weight_limit * num_crates)
    
    return weight_left_out

print(solution())