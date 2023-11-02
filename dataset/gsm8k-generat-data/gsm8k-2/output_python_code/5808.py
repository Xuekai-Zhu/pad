def solution():
    """Daryl is loading crates at a warehouse and wants to make sure that they are not overloaded. Each crate can weigh up to 20kg and he has 15 crates he can fill. He has 4 bags of nails to load, each of which weighs 5kg; he has 12 bags of hammers, each of which weighs 5 kg; he also has 10 bags of wooden planks, each of which weighs 30kg and can be sub-divided. He realizes that he has too much to load and will have to leave some items out of the crates to meet the weight limit. In kg, how much is Daryl going to have to leave out of the crates?"""
    crate_weight_limit = 20
    number_of_crates = 15
    crate_capacity = crate_weight_limit * number_of_crates
    nails_weight = 5 * 4
    hammers_weight = 5 * 12
    planks_weight = 10 * 30
    total_weight = nails_weight + hammers_weight + planks_weight
    excess_weight = total_weight - crate_capacity
    result = excess_weight
    return result

print(solution())