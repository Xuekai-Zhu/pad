def solution():
    
    # Define the number of madeleine cookies Shannon wants to make
    madeleine_cookies = 30

    # Define the number of madeleine cookies Shannon eats as a treat
    treat_cookies = 2 * madeleine_cookies

    # Define the number of cookies Shannon's recipe makes in 30 days
    recipe_cookies = 1 * 12

    # Calculate the number of cookies Shannon needs to make
    remaining_cookies = madeleine_cookies - treat_cookies - recipe_cookies

    # Calculate the number of dozens of cookies Shannon needs to make
    dozens_of_cookies = remaining_cookies / recipe_cookies

    # Display the number of dozens of cookies Shannon needs to make
    result = dozens_of_cookies
    return result

print(solution())