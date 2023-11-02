def solution():
    alice_cookies = 74  # Alice baked 74 chocolate chip cookies
    bob_cookies = 7  # Bob baked 7 peanut butter cookies

    alice_cookies += 5  # Alice baked 5 more cookies
    bob_cookies += 36  # Bob baked 36 more cookies

    total_cookies = alice_cookies + bob_cookies  # Total number of cookies they had

    thrown_on_floor = total_cookies - 93  # Difference between total cookies and number of edible cookies

    result = thrown_on_floor
    return result

print(solution())