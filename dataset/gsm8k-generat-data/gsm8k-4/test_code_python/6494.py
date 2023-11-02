def solution():
    """Donna is trying to figure out if her truck is over a particular bridge's weight limit. The bridge can hold 20,000 pounds. Donna's empty truck weighs 12,000 pounds. She's carrying 20 crates of soda that each weigh 50 pounds, 3 dryers that each weigh 3000 pounds, and twice as much weight in fresh produce as in soda. How much does Donna's fully loaded truck weigh?"""
    # Define the weight limit of the bridge and the weight of Donna's empty truck
    weight_limit = 20000
    empty_weight = 12000

    # Calculate the weight of the soda crates
    soda_weight = 20 * 50

    # Calculate the weight of the dryers
    dryer_weight = 3 * 3000

    # Calculate the weight of the fresh produce
    produce_weight = 2 * soda_weight

    # Calculate the total weight of the loaded truck
    total_weight = empty_weight + soda_weight + dryer_weight + produce_weight

    # Check if the loaded truck is over the weight limit of the bridge
    if total_weight > weight_limit:
        result = "Overweight"
    else:
        result = total_weight
    return result

print(solution())