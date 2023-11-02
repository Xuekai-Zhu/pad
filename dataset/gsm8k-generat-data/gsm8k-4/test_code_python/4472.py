def solution():
    """Crackers contain 15 calories each and cookies contain 50 calories each. If Jimmy eats 7 cookies, how many crackers does he need to eat to have consumed a total of 500 calories?"""
    # Define the calorie count for crackers and cookies
    CRACKER_CALORIES = 15
    COOKIE_CALORIES = 50

    # Define the number of cookies Jimmy ate
    num_cookies = 7

    # Calculate the total calories consumed from cookies
    total_calories = num_cookies * COOKIE_CALORIES

    # Calculate the number of crackers Jimmy needs to eat to reach 500 calories
    num_crackers = (500 - total_calories) // CRACKER_CALORIES

    # return the result
    result = num_crackers
    return result

print(solution())