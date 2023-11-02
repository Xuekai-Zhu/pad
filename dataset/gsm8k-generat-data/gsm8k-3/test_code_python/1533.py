def solution():
    """Jen bought a bag of cookies and ate three-quarters of the bag that day. The next day, she ate half of the remaining cookies. She has 8 cookies left on the third day. How many cookies were in the bag to start?"""
    # Define the variables
    cookies_start = None
    cookies_day1 = None
    cookies_day2 = None
    cookies_day3 = 8
    
    # Calculate the number of cookies on Day 2
    cookies_day2 = (cookies_day1 - cookies_day3) * 2
    
    # Calculate the number of cookies on Day 1
    cookies_day1 = cookies_start * 0.75
    
    # Calculate the number of cookies in the bag to start
    cookies_start = cookies_day1 + cookies_day2 + cookies_day3
    
    # Display the number of cookies in the bag to start
    result = int(cookies_start)
    return result

print(solution())