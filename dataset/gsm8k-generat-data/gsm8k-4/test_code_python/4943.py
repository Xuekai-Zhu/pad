def solution():
    """Juan needs 10 half-gallons of milk to bake 40 cookies with. How many half-gallons of milk does Juan need to bake 200 dozen cookies?"""
    # Define the initial number of cookies and the corresponding milk needed
    initial_cookies = 40
    initial_milk = 10

    # Define the target number of cookies
    target_cookies = 200 * 12

    # Calculate the milk needed for the target number of cookies
    target_milk = (target_cookies * initial_milk) / initial_cookies

    result = target_milk
    return result

print(solution())