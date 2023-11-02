def solution():
    """Yanna baked twenty butter cookies and forty biscuits in the morning. In the afternoon, she baked ten butter cookies and twenty biscuits. How many more biscuits did she bake than butter cookies?"""
    # Define the initial number of butter cookies and biscuits
    butter_cookies = 20
    biscuits = 40

    # Add the number of butter cookies and biscuits baked in the afternoon
    butter_cookies += 10
    biscuits += 20

    # Calculate the difference between the number of biscuits and butter cookies
    difference = biscuits - butter_cookies

    # return the result
    result = difference
    return result

print(solution())