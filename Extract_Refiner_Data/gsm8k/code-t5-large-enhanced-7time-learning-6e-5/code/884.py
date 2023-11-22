def solution():
    
    # Define the total number of cookies
    total_cookies = 55

    # Define the number of cookies eaten
    cookies_eaten = 5

    # Calculate the number of cookies left
    cookies_left = total_cookies - cookies_eaten

    # Calculate the number of cookies in each jar
    cookies_per_jar = cookies_left / 5

    # Display the number of cookies in each jar
    result = cookies_per_jar
    return result

print(solution())