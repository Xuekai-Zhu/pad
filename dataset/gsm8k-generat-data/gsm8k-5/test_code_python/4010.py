def solution():
    batches = 4 * 2  # Beth bakes 4, 2 dozen batches of cookies
    cookies_per_batch = 24  # Each batch contains 2 dozen cookies (24 cookies)
    total_cookies = batches * cookies_per_batch  # Calculate the total number of cookies baked

    people = 16  # The cookies are shared amongst 16 people equally
    cookies_per_person = total_cookies / people  # Calculate the number of cookies each person consumes

    result = cookies_per_person
    return result

print(solution())