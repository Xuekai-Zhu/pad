def solution():
    """Crackers contain 15 calories each and cookies contain 50 calories each. If Jimmy eats 7 cookies, how many crackers does he need to eat to have consumed a total of 500 calories?"""
    # Define the number of calories per cracker and cookie
    CRACKER_CALORIES = 15
    COOKIE_CALORIES = 50

    # Define the number of cookies Jimmy ate
    cookies = 7

    # Calculate the total number of calories from the cookies Jimmy ate
    cookie_calories = cookies * COOKIE_CALORIES

    # Calculate the number of crackers Jimmy needs to eat to consume a total of 500 calories
    crackers_needed = (500 - cookie_calories) // CRACKER_CALORIES

    # Display the number of crackers Jimmy needs to eat
    result = crackers_needed
    return result

print(solution())