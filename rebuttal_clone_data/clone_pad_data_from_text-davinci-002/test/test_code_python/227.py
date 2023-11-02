def solution():
     total_cookies = 256
     cookies_given_to_tim = 15
     cookies_given_to_mike = 23
     cookies_given_to_anna = 2 * cookies_given_to_tim
     cookies_in_fridge = total_cookies - cookies_given_to_tim - cookies_given_to_mike - cookies_given_to_anna
     result = cookies_in_fridge
     return result

print(solution())