def solution():
    alice_cookies = 74
    bob_cookies = 7
    alice_additional_cookies = 5
    bob_additional_cookies = 36
    total_edible_cookies = 93

    # Calculate the total number of cookies baked before adding additional cookies
    total_baked_cookies = alice_cookies + bob_cookies

    # Calculate the total number of cookies baked after adding additional cookies
    total_baked_cookies += alice_additional_cookies + bob_additional_cookies

    # Calculate the number of cookies thrown on the floor
    num_thrown_cookies = total_baked_cookies - total_edible_cookies
    result = num_thrown_cookies
    return result

print(solution())