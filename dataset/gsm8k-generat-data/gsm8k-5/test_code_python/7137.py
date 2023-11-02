def solution():
    total_macaroons = 12
    macaroon_weight = 5  # Each macaroon weighs 5 ounces
    num_bags = 4
    macaroons_per_bag = total_macaroons / num_bags

    # Calculate the total weight of macaroons before Steve ate one bag
    total_weight_before = total_macaroons * macaroon_weight

    # Calculate the weight of macaroons in one bag
    bag_weight = macaroons_per_bag * macaroon_weight

    # Calculate the new total weight of macaroons after Steve ate one bag
    total_weight_now = total_weight_before - bag_weight
    result = total_weight_now
    return result

print(solution())