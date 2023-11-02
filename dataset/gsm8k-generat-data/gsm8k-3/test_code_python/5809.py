def solution():
    """Daryl wants to make sure that the loaded crates do not exceed the weight limit. Each crate can weigh up to 20kg and he has 15 of them to fill. He has 4 bags of nails weighing 5kg each, 12 bags of hammers weighing 5kg each, and 10 bags of wooden planks weighing 30kg each. How much weight will he have to leave out to meet the limit?"""
    # Define the weight limit per crate
    CRATE_LIMIT = 20

    # Define the number and weight of bags of nails
    nails_num = 4
    nails_weight = 5

    # Define the number and weight of bags of hammers
    hammers_num = 12
    hammers_weight = 5

    # Define the number and weight of bags of wooden planks
    planks_num = 10
    planks_weight = 30

    # Calculate the maximum weight that can be loaded in the crates
    max_weight = CRATE_LIMIT * 15

    # Calculate the weight of all the items to be loaded
    total_weight = (nails_num * nails_weight) + (hammers_num * hammers_weight) + (planks_num * planks_weight)

    # Calculate the weight that needs to be left out
    left_out_weight = total_weight - max_weight

    # Display the weight that needs to be left out
    result = left_out_weight
    return result

print(solution())