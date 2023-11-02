def solution():
    """Karen bakes 50 chocolate chip cookies. She keeps 10 for herself, and she gives 8 to her grandparents. If Karen wants to give everyone in her class cookies, and there are 16 people in her class, how many cookies will each person receive?"""
    total_cookies = 50
    kept_cookies = 10
    grandparents_cookies = 8
    remaining_cookies = total_cookies - kept_cookies - grandparents_cookies
    class_size = 16
    cookies_per_person = remaining_cookies / class_size
    result = cookies_per_person
    return result

print(solution())