def solution():
    """Beth bakes 4, 2 dozen batches of cookies in a week. If these cookies are shared amongst 16 people equally, how many cookies does each person consume?"""
    batches = 4
    dozen = 2
    cookies_per_batch = 12  # since one dozen equals 12
    total_cookies = batches * dozen * cookies_per_batch
    people = 16
    cookies_per_person = total_cookies / people
    result = cookies_per_person
    return result

print(solution())