def solution():
    """Yanna baked twenty butter cookies and forty biscuits in the morning. In the afternoon, she baked ten butter cookies and twenty biscuits. How many more biscuits did she bake than butter cookies?"""
    # Define the number of butter cookies and biscuits baked in the morning
    butter_cookies_morning = 20
    biscuits_morning = 40

    # Define the number of butter cookies and biscuits baked in the afternoon
    butter_cookies_afternoon = 10
    biscuits_afternoon = 20

    # Calculate the total number of butter cookies and biscuits baked
    total_butter_cookies = butter_cookies_morning + butter_cookies_afternoon
    total_biscuits = biscuits_morning + biscuits_afternoon

    # Calculate the difference between the number of biscuits and butter cookies
    biscuits_difference = total_biscuits - total_butter_cookies

    # Display the difference
    result = biscuits_difference
    return result

print(solution())