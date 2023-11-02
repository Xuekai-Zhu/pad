def solution():
    total_cookies = 70  # There are 70 cookies in a jar
    remaining_cookies = 28  # After a week, there are 28 cookies left
    cookies_taken = (total_cookies - remaining_cookies) / 7  # Paul took out the same amount each day
    cookies_taken_in_4_days = cookies_taken * 4  # Paul took out cookies for 4 days
    
    result = cookies_taken_in_4_days
    return result

print(solution())