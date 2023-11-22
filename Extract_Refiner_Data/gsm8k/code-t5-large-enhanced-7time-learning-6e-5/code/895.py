def solution():
    
    # Define the total number of cookies
    total_cookies = 100

    # Calculate the number of cookies each nephew will get
    cookies_per_nephew = total_cookies / 6

    # Subtract the cookies snuck by Susband
    cookies_after_husband = cookies_per_nephew - 4

    # Display the number of cookies each nephew will get
    result = cookies_after_husband
    return result

print(solution())