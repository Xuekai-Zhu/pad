def solution():
    """Beth bakes 4, 2 dozen batches of cookies in a week. If these cookies are shared amongst 16 people equally, how many cookies does each person consume?"""
    # Define the number of cookies baked
    num_cookies = 4 * 2 * 12

    # Calculate the number of cookies each person consumes
    cookies_per_person = num_cookies / 16

    # return the result
    result = cookies_per_person
    return result

print(solution())