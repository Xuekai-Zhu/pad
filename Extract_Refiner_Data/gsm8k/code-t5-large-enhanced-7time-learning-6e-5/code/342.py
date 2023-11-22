def solution():
    
    # Define the number of cookies in the bag
    COOKIES_PER_BAG = 36

    # Define the number of cookies Jenny puts in her son's lunch box
    lunch_cookies = 4

    # Define the number of days Jenny's lunch box has been put
    lunch_days = 5

    # Define the number of cookies Jenny's husband eats each day
    husband_cookies = 1

    # Calculate the total number of cookies Jenny has
    total_cookies = COOKIES_PER_BAG + lunch_cookies * lunch_days

    # Calculate the number of cookies Jenny's husband eats
    husband_cookies_eaten = husband_cookies * 7

    # Calculate the number of cookies Jenny eats
    jenny_cookies_eaten = total_cookies - husband_cookies_eaten

    # Display the number of cookies Jenny eats
    result = jenny_cookies_eaten

print(solution())