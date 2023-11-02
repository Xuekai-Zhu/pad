def solution():
    cookies_per_pound = 12
    pounds_of_flour_used = 2
    bags_of_flour = 4
    pounds_per_bag = 5
    total_cookies = cookies_per_pound * pounds_of_flour_used
    cookies_eaten = 15
    cookies_left = total_cookies - cookies_eaten
    result = cookies_left
    return result

print(solution())