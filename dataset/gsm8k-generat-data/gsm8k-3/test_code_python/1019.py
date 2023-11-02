def solution():
    """Alice and Bob decided to bake cookies for their first date. Alice baked 74 chocolate chip cookies and Bob baked 7 peanut butter cookies. After accidentally throwing some on the floor, Alice baked 5 more cookies and Bob baked 36 more. If they had 93 edible cookies at the end, how many were accidentally thrown on the floor?"""
    # Define the initial number of cookies baked
    alice_cookies = 74
    bob_cookies = 7

    # Bake some more cookies
    alice_cookies += 5
    bob_cookies += 36

    # Calculate the total number of cookies
    total_cookies = alice_cookies + bob_cookies

    # Calculate the number of cookies thrown on the floor
    thrown_cookies = total_cookies - 93

    # Display the number of cookies thrown on the floor
    result = thrown_cookies
    return result

print(solution())