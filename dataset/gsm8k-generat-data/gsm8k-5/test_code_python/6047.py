def solution():
    # Calculate the total number of baked goods
    total_cookies_and_brownies = 60 + 32

    # Calculate the total number of baked goods after Kyle and his mom eat some
    remaining_cookies_and_brownies = total_cookies_and_brownies - 2 - 2 - 1 - 2

    # Calculate the total amount of money Kyle will make from selling cookies and brownies
    total_money =  (remaining_cookies_and_brownies - 32) * 1 + 32 * 1.5
    result = total_money
    return result

print(solution())