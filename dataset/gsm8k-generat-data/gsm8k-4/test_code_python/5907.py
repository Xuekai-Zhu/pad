def solution():
    """Jenny brought in 40 peanut butter cookies and 50 chocolate chip cookies for the bake sale. Marcus brought in 30 peanut butter cookies and and 20 lemon cookies. If Renee, who's allergic to peanuts, picks a cookie at random, what is the chance she'll have an allergic reaction expressed as a percentage?"""
    # Define the total number of peanut butter cookies
    peanut_butter_cookies = 40 + 30

    # Define the total number of cookies
    total_cookies = peanut_butter_cookies + 50 + 20

    # Calculate the probability of Renee picking a peanut butter cookie
    probability = peanut_butter_cookies / total_cookies

    # Convert the probability to a percentage
    percentage = probability * 100

    # Round the result to the nearest whole number
    result = round(percentage)
    return result

print(solution())