def solution():
    # Define the initial number of cookies in the jar
    initial_cookies = 10

    # Calculate the total number of cookies taken out of the jar
    total_cookies_taken = 3 + 3 + 7

    # Calculate the number of cookies that Lou Senior put back
    cookies_put_back = 2

    # Calculate the number of cookies remaining in the jar
    cookies_remaining = initial_cookies - total_cookies_taken + cookies_put_back

    result = cookies_remaining
    return result

print(solution())