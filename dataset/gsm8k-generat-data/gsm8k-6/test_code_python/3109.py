def solution():
    # Calculate the number of cookies remaining in the jar
    initial_cookies = 10  # assume there were 10 cookies in the jar initially
    eaten_cookies = 3 + 2 - 2 + 7  # Lou Senior took 3 cookies and ate them, took 3 more but put back 2, Louie Junior took 7 cookies
    remaining_cookies = initial_cookies - eaten_cookies
    result = remaining_cookies
    return result

print(solution())