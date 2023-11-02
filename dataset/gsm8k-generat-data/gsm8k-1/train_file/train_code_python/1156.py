def solution():
    """Tony's dad is very strict about the washing machine and family members are only allowed to wash 50 total ounces of clothing at a time. Tony doesn't want to break the rules, so he weighs his clothes and finds that a pair of socks weighs 2 ounces, underwear weighs 4 ounces, a shirt weighs 5 ounces, shorts weigh 8 ounces, and pants weigh 10 ounces. Tony is washing a pair of pants, 2 shirts, a pair of shorts, and 3 pairs of socks. How many more pairs of underwear can he add to the wash and not break the rule?"""
    weight_pair_socks = 2
    weight_underwear = 4
    weight_shirt = 5
    weight_shorts = 8
    weight_pants = 10
    total_weight_used = (weight_pants * 1) + (weight_shorts * 1) + (weight_shirt * 2) + (weight_pair_socks * 3)
    max_weight_allowed = 50
    remaining_weight_allowed = max_weight_allowed - total_weight_used
    max_pairs_of_underwear = remaining_weight_allowed // weight_underwear
    result = max_pairs_of_underwear
    return result

print(solution())