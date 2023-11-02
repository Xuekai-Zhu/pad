def solution():
    # Calculate the total number of cookies taken by all the neighbors except Sarah
    total_cookies = 15 * 10  # 15 neighbors each took 10 cookies

    # Calculate how many cookies Sarah took
    sarah_cookies = total_cookies - 8  # there were only 8 cookies left when the last neighbor arrived

    # Calculate how many cookies Sarah should have taken
    correct_cookies = (150 - 8) / 15  # 150 cookies total minus 8 left over, divided by 15 neighbors

    # Calculate how many extra cookies Sarah took
    extra_cookies = sarah_cookies - correct_cookies

    result = extra_cookies
    return result

print(solution())