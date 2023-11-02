def solution():
    """Donna is trying to figure out if her truck is over a particular bridge's weight limit. The bridge can hold 20,000 pounds. Donna's empty truck weighs 12,000 pounds. She's carrying 20 crates of soda that each weigh 50 pounds, 3 dryers that each weigh 3000 pounds, and twice as much weight in fresh produce as in soda. How much does Donna's fully loaded truck weigh?"""
    # Define the weight limit of the bridge
    WEIGHT_LIMIT = 20000

    # Define the weight of the empty truck and the weight of each item
    EMPTY_TRUCK_WEIGHT = 12000
    SODA_WEIGHT = 50
    DRYER_WEIGHT = 3000

    # Define the number of items Donna is carrying
    num_soda_crates = 20
    num_dryers = 3

    # Calculate the total weight of the soda
    soda_weight = num_soda_crates * SODA_WEIGHT

    # Calculate the total weight of the dryers
    dryer_weight = num_dryers * DRYER_WEIGHT

    # Calculate the total weight of the fresh produce
    fresh_produce_weight = 2 * soda_weight

    # Calculate the total weight of the fully loaded truck
    total_weight = EMPTY_TRUCK_WEIGHT + soda_weight + dryer_weight + fresh_produce_weight

    # Check if the fully loaded truck is over the weight limit
    if total_weight > WEIGHT_LIMIT:
        result = "The truck is over the weight limit!"
    else:
        result = total_weight

    return result

print(solution())