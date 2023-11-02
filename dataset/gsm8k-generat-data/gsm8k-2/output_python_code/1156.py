def solution():
    """Tony's dad is very strict about the washing machine and family members are only allowed to wash 50 total ounces of clothing at a time. Tony doesn't want to break the rules, so he weighs his clothes and finds that a pair of socks weighs 2 ounces, underwear weighs 4 ounces, a shirt weighs 5 ounces, shorts weigh 8 ounces, and pants weigh 10 ounces. Tony is washing a pair of pants, 2 shirts, a pair of shorts, and 3 pairs of socks. How many more pairs of underwear can he add to the wash and not break the rule?"""
    total_weight = 0
    pants_weight = 10
    shirts_weight = 2 * 5
    shorts_weight = 8
    socks_weight = 3 * 2
    total_weight = pants_weight + shirts_weight + shorts_weight + socks_weight
    max_weight = 50
    remaining_weight = max_weight - total_weight
    underwear_weight = 4
    max_undies = remaining_weight // underwear_weight
    result = max_undies
    return result

print(solution())