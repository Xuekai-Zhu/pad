def solution():
    """Juan needs 10 half-gallons of milk to bake 40 cookies with. How many half-gallons of milk does Juan need to bake 200 dozen cookies?"""
    
    # Calculate the number of cookies in 200 dozen
    cookies = 200 * 12

    # Calculate the number of half-gallons of milk needed for 40 cookies
    milk_for_40_cookies = 10

    # Calculate the number of half-gallons of milk needed for the total number of cookies
    milk_for_all_cookies = (cookies/40) * milk_for_40_cookies

    # Round the answer to the nearest half-gallon
    milk_needed = round(milk_for_all_cookies * 2) / 2

    # Display the number of half-gallons of milk needed
    result = milk_needed
    return result

print(solution())