def solution():
    """Beth bakes 4, 2 dozen batches of cookies in a week.  If these cookies are shared amongst 16 people equally, how many cookies does each person consume?"""
    # Define the number of cookies in a dozen
    cookies_per_dozen = 12

    # Define the number of cookie batches
    num_batches = 4

    # Calculate the total number of cookies baked
    total_cookies = num_batches * 2 * cookies_per_dozen

    # Calculate the number of cookies each person consumes
    cookies_per_person = total_cookies // 16

    # Display the number of cookies each person consumes
    result = cookies_per_person
    return result

print(solution())