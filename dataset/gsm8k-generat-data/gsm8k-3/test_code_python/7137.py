def solution():
    """John bakes 12 coconut macaroons, each weighing 5 ounces. He then packs an equal number of the macaroons in 4 different brown bags, ready for delivery. When he briefly leaves the kitchen to pick the phone, his little brother Steve eats the entire contents of one of the brown bags.  What is the total weight, in ounces, of the remaining coconut macaroons?"""
    # Define the number of macaroons and the weight per macaroon
    MACAROON_COUNT = 12
    MACAROON_WEIGHT = 5

    # Calculate the total weight of all the macaroons
    total_weight = MACAROON_COUNT * MACAROON_WEIGHT

    # Calculate the number of macaroons in each brown bag
    macaroons_per_bag = MACAROON_COUNT // 4

    # Calculate the weight of each brown bag
    bag_weight = macaroons_per_bag * MACAROON_WEIGHT

    # Calculate the weight of the remaining macaroons
    remaining_weight = total_weight - (3 * bag_weight) - (MACAROON_COUNT - macaroons_per_bag) * MACAROON_WEIGHT

    # Display the total weight of the remaining macaroons
    result = remaining_weight
    return result

print(solution())