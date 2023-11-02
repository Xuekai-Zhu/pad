def solution():
    total_cookies = 150
    cookies_per_person = 10
    cookies_left = 8
    people = 15
    cookies_taken = total_cookies - cookies_left
    cookies_Sarah_took = cookies_taken - (people - 1) * cookies_per_person
    result = cookies_Sarah_took
    return result

print(solution())