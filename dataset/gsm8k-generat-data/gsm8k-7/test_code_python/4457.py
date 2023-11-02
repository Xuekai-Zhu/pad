def solution():
    pounds_per_dozen = 2
    bags_of_flour = 4
    pounds_per_bag = 5
    cookies_per_dozen = 12
    cookies_eaten = 15

    # Calculate the total pounds of flour used
    total_pounds = bags_of_flour * pounds_per_bag

    # Calculate the number of dozens of cookies Matt can make
    dozens_of_cookies = total_pounds / pounds_per_dozen

    # Calculate the total number of cookies Matt can make
    total_cookies = dozens_of_cookies * cookies_per_dozen

    # Calculate the number of cookies left after Jim eats 15
    cookies_left = total_cookies - cookies_eaten
    result = cookies_left
    return result

print(solution())