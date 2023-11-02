def solution():
    """A bag of chips weighs 20 ounces, and a tin of cookies weighs 9 ounces. If Jasmine buys 6 bags of chips and 4 times as many tins of cookies, how many pounds does she have to carry?"""
    chips_weight = 20 * 6  # 6 bags of chips
    cookies_weight = 9 * 4 * 6  # 4 times as many tins of cookies as bags of chips, and 6 bags of chips
    total_weight = (chips_weight + cookies_weight) / 16  # convert ounces to pounds
    result = total_weight
    return result

print(solution())