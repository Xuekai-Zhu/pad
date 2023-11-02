def solution():
    """Daryl is loading crates at a warehouse and wants to make sure that they are not overloaded. Each crate can weigh up to 20kg and he has 15 crates he can fill. He has 4 bags of nails to load, each of which weighs 5kg; he has 12 bags of hammers, each of which weighs 5 kg; he also has 10 bags of wooden planks, each of which weighs 30kg and can be sub-divided. He realizes that he has too much to load and will have to leave some items out of the crates to meet the weight limit. In kg, how much is Daryl going to have to leave out of the crates?"""
    # Define the weight limit per crate
    WEIGHT_LIMIT = 20

    # Define the number of crates
    NUM_CRATES = 15

    # Calculate the total weight of the nails
    total_nails_weight = 4 * 5

    # Calculate the total weight of the hammers
    total_hammers_weight = 12 * 5

    # Calculate the total weight of the wooden planks
    total_wooden_planks_weight = 10 * 30

    # Calculate the maximum weight that can be loaded in the crates
    max_load_weight = NUM_CRATES * WEIGHT_LIMIT

    # Calculate the total weight of all the items
    total_weight = total_nails_weight + total_hammers_weight + total_wooden_planks_weight

    # Calculate the weight that needs to be left out
    left_out_weight = total_weight - max_load_weight

    # return the result
    result = left_out_weight
    return result

print(solution())