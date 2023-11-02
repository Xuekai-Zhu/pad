def solution():
    # Calculate the total number of peanut butter cookies
    total_peanut_butter = 40 + 30  # Jenny brought in 40 and Marcus brought in 30

    # Calculate the total number of cookies
    total_cookies = 40 + 50 + 30 + 20  # Jenny brought in 40 peanut butter and 50 chocolate chip cookies, Marcus brought in 30 peanut butter and 20 lemon cookies

    # Calculate the probability of Renee picking a peanut butter cookie
    probability = total_peanut_butter / total_cookies

    # Express the probability as a percentage
    percentage = probability * 100

    result = percentage
    return result

print(solution())