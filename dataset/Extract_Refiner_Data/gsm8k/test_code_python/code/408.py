def solution():
    
    # Define the number of cookies Shannon needs per day
    COOKIES_PER_DAY = 2

    # Define the number of days Shannon wants to make cookies
    DAYS = 30

    # Define the number of cookies Shannon's recipe needs to make
    RECIPE_COOKIES = 12

    # Calculate the total number of cookies Shannon needs to make
    total_cookies = COOKIES_PER_DAY * DAYS

    # Calculate the number of dozens of cookies Shannon needs to make
    dozens_needed = total_cookies / RECIPE_COOKIES

    # Display the number of dozens of cookies Shannon needs to make
    result = dozens_needed
    return result

print(solution())