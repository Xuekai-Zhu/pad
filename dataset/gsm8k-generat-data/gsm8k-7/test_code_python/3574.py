def solution():
    num_cookies = 60
    nuts_ratio = 0.25
    chocolate_ratio = 0.4

    # Calculate the number of cookies with nuts only
    nuts_cookies = int(num_cookies * nuts_ratio)

    # Calculate the number of cookies with chocolate chips only
    chocolate_cookies = int(num_cookies * chocolate_ratio)

    # Calculate the number of cookies with both nuts and chocolate chips
    nuts_and_chocolate_cookies = num_cookies - nuts_cookies - chocolate_cookies

    # Calculate the total number of nuts needed
    total_nuts = (nuts_cookies + nuts_and_chocolate_cookies) * 2
    result = total_nuts
    return result

print(solution())