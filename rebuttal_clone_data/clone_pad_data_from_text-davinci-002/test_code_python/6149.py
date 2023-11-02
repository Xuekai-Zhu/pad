def solution():
     chips_per_bag = 20
     cookies_per_tin = 9
     bags_of_chips = 6
     tins_of_cookies = bags_of_chips * 4
     total_ounces = (chips_per_bag * bags_of_chips) + (cookies_per_tin * tins_of_cookies)
     total_pounds = total_ounces / 16
     result = total_pounds
     return result

print(solution())