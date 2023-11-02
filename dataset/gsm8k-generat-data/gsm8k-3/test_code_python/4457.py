def solution():
    """Matt can make a batch of a dozen cookies using 2 pounds of flour.  He uses 4 bags of flour each weighing 5 pounds.  If Jim eats 15 cookies how many cookies are left?"""
    # Calculate the total amount of flour used
    total_flour = 4 * 5 # 4 bags of flour, each weighing 5 pounds

    # Calculate the number of dozens of cookies made
    dozens_of_cookies = total_flour // 2

    # Calculate the total number of cookies made
    total_cookies = dozens_of_cookies * 12

    # Calculate the number of cookies Jim didn't eat
    cookies_left = total_cookies - 15

    # Display the number of cookies left
    result = cookies_left
    return result

print(solution())