def solution():
    """Jenny brought in 40 peanut butter cookies and 50 chocolate chip cookies for the bake sale. Marcus brought in 30 peanut butter cookies and and 20 lemon cookies. If Renee, who's allergic to peanuts, picks a cookie at random, what is the chance she'll have an allergic reaction expressed as a percentage?"""
    # Define the total number of peanut butter cookies
    PB_COOKIES = 40 + 30

    # Define the total number of cookies
    TOTAL_COOKIES = 40 + 50 + 30 + 20

    # Calculate the probability of Renee picking a peanut butter cookie
    probability = PB_COOKIES / TOTAL_COOKIES * 100

    # Display the probability as a percentage
    result = probability
    return result

print(solution())