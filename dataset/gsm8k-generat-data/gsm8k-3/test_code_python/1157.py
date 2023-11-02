def solution():
    """Tony's dad is very strict about the washing machine and family members are only allowed to wash 50 total ounces of clothing at a time. Tony doesn't want to break the rules, so he weighs his clothes and finds that a pair of socks weighs 2 ounces, underwear weighs 4 ounces, a shirt weighs 5 ounces, shorts weigh 8 ounces, and pants weigh 10 ounces. Tony is washing a pair of pants, 2 shirts, a pair of shorts, and 3 pairs of socks. How many more pairs of underwear can he add to the wash and not break the rule?"""
    # Define the weight of each type of clothing
    SOCK_WEIGHT = 2
    UNDERWEAR_WEIGHT = 4
    SHIRT_WEIGHT = 5
    SHORTS_WEIGHT = 8
    PANTS_WEIGHT = 10

    # Calculate the total weight of the clothes Tony is already washing
    total_weight = (1 * PANTS_WEIGHT) + (2 * SHIRT_WEIGHT) + (1 * SHORTS_WEIGHT) + (3 * SOCK_WEIGHT)

    # Calculate the remaining weight Tony can add to the wash
    remaining_weight = 50 - total_weight

    # Calculate the number of pairs of underwear Tony can add to the wash without going over the weight limit
    underwear_pairs = remaining_weight // UNDERWEAR_WEIGHT

    # Display the maximum number of pairs of underwear Tony can add to the wash
    result = underwear_pairs
    return result

print(solution())