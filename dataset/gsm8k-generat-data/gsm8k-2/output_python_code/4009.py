def solution():
    """Beth bakes 4, 2 dozen batches of cookies in a week. If these cookies are shared amongst 16 people equally, how many cookies does each person consume?"""
    batches = 4 * 2
    cookies = batches * 12
    people = 16
    cookies_per_person = cookies / people
    result = cookies_per_person
    return result

print(solution())