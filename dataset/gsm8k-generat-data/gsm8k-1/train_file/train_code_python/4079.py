def solution():
    """Karen bakes 50 chocolate chip cookies. She keeps 10 for herself, and she gives 8 to her grandparents. If Karen wants to give everyone in her class cookies, and there are 16 people in her class, how many cookies will each person receive?"""
    total_cookies = 50
    cookies_kept = 10
    cookies_given = 8
    cookies_left = total_cookies - (cookies_kept + cookies_given)
    cookies_per_person = cookies_left // 16
    result = cookies_per_person
    return result

print(solution())