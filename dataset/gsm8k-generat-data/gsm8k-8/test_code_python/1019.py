def solution():
    # Define Alice and Bob's initial cookie quantities
    alice_cookies = 74
    bob_cookies = 7

    # Define the additional cookies baked after some were thrown on the floor
    alice_add_cookies = 5
    bob_add_cookies = 36

    # Calculate the total number of cookies before some were thrown on the floor
    total_cookies = alice_cookies + bob_cookies

    # Calculate the total number of cookies after additional cookies were baked
    total_edible_cookies = alice_cookies + alice_add_cookies + bob_cookies + bob_add_cookies

    # Calculate the number of cookies thrown on the floor
    thrown_cookies = total_cookies - total_edible_cookies + 93

    result = thrown_cookies
    return result

print(solution())