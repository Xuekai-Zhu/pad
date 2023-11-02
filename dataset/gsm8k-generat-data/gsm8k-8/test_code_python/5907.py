def solution():
    # Calculate the total number of peanut butter cookies and the total number of cookies
    peanut_butter_cookies = 40 + 30
    total_cookies = peanut_butter_cookies + 50 + 20

    # Calculate the probability that Renee picks a peanut butter cookie
    p_peanut_butter = peanut_butter_cookies / total_cookies

    # Convert the probability to a percentage
    percentage = p_peanut_butter * 100

    result = percentage
    return result

print(solution())