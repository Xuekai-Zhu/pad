def solution():
    # Define the initial number of cookies
    initial_cookies = 5 * 12

    # Calculate the number of cookies sold to Mr. Stone
    cookies_sold_to_mr_stone = 2 * 12

    # Calculate the number of cookies sold to Brock
    cookies_sold_to_brock = 7

    # Calculate the number of cookies sold to Katy
    cookies_sold_to_katy = 2 * cookies_sold_to_brock

    # Calculate the total number of cookies sold
    total_cookies_sold = cookies_sold_to_mr_stone + cookies_sold_to_brock + cookies_sold_to_katy

    # Calculate the number of cookies left
    cookies_left = initial_cookies - total_cookies_sold
    result = cookies_left
    return result

print(solution())