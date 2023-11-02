def solution():
    # Calculate the total amount of flour Matt has
    total_flour = 4 * 5  # Matt uses 4 bags of flour each weighing 5 pounds

    # Calculate the number of dozens of cookies Matt can make
    dozens_of_cookies = total_flour // 2

    # Calculate the total number of cookies Matt can make
    total_cookies = dozens_of_cookies * 12

    # Calculate the number of cookies left after Jim eats 15
    cookies_left = total_cookies - 15
    result = cookies_left
    return result

print(solution())