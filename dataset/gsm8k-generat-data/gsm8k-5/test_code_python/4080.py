def solution():
    total_cookies = 50  # Karen bakes 50 chocolate chip cookies
    cookies_kept = 10  # Karen keeps 10 for herself
    cookies_given_away = 8  # Karen gives 8 to her grandparents
    cookies_left_to_share = total_cookies - cookies_kept - cookies_given_away  # Karen has this many cookies left to share

    # Calculate the number of cookies each person in Karen's class will receive
    cookies_per_person = cookies_left_to_share / 16
    result = cookies_per_person
    return result

print(solution())