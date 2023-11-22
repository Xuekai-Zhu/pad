def solution():
    
    # Define the initial number of cookies
    initial_cookies = 23 + 42

    # Define the number of cookies eaten by the brother
    brother_cookies = 44

    # Calculate the number of cookies left for Rachel
    remaining_cookies = initial_cookies - 42 - brother_cookies

    # Display the number of cookies left for Rachel
    result = remaining_cookies
    return result

print(solution())