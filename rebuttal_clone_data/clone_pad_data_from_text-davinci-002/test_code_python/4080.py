def solution():
    cookies_baked = 50
    cookies_kept = 10
    cookies_given = 8
    cookies_left = cookies_baked - cookies_kept - cookies_given
    people_in_class = 16
    cookies_per_person = cookies_left / people_in_class
    result = cookies_per_person
    return result

print(solution())