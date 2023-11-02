def solution():
    """John bakes 12 coconut macaroons, each weighing 5 ounces. He then packs an equal number of the macaroons in 4 different brown bags, ready for delivery. When he briefly leaves the kitchen to pick the phone, his little brother Steve eats the entire contents of one of the brown bags. What is the total weight, in ounces, of the remaining coconut macaroons?"""
    # Define the number of macaroons and their weight
    num_macaroons = 12
    macaroon_weight = 5

    # Calculate the total weight of all the macaroons
    total_weight = num_macaroons * macaroon_weight

    # Calculate the weight of one brown bag
    bag_weight = total_weight / 4

    # Subtract the weight of the eaten bag from the total weight
    remaining_weight = total_weight - bag_weight

    # Return the remaining weight in ounces
    result = remaining_weight
    return result

print(solution())