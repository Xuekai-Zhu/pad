def solution():
    num_cookies_initial = 0
    num_cookies_eaten_day1 = 3
    num_cookies_eaten_day2 = 2
    num_cookies_hidden_by_louie = 7

    # Calculate the total number of cookies eaten by Lou Senior
    total_cookies_eaten = num_cookies_eaten_day1 + num_cookies_eaten_day2

    # Calculate the total number of cookies left in the jar after Lou Senior ate some
    num_cookies_initial = total_cookies_eaten + num_cookies_hidden_by_louie

    # Calculate the number of cookies left after Debra accused Lou Senior of eating half
    num_cookies_left = num_cookies_initial / 2
    result = num_cookies_left
    return result

print(solution())