def solution():
    """Tony's dad is very strict about the washing machine and family members are only allowed to wash 50 total ounces of clothing at a time. Tony doesn't want to break the rules, so he weighs his clothes and finds that a pair of socks weighs 2 ounces, underwear weighs 4 ounces, a shirt weighs 5 ounces, shorts weigh 8 ounces, and pants weigh 10 ounces. Tony is washing a pair of pants, 2 shirts, a pair of shorts, and 3 pairs of socks. How many more pairs of underwear can he add to the wash and not break the rule?"""
    # Define the weights of each type of clothing
    socks_weight = 2
    underwear_weight = 4
    shirt_weight = 5
    shorts_weight = 8
    pants_weight = 10

    # Calculate the total weight of clothing Tony wants to wash
    total_weight = (1 * pants_weight) + (2 * shirt_weight) + (1 * shorts_weight) + (3 * socks_weight)

    # Calculate the remaining weight Tony can add to the washing machine
    remaining_weight = 50 - total_weight

    # Calculate the maximum number of pairs of underwear that can be added
    max_underwear = remaining_weight // underwear_weight

    # return the result
    result = max_underwear
    return result

print(solution())