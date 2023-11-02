def solution():
    # Calculate the number of cookies Karen has left after keeping some and giving some away
    remaining_cookies = 50 - 10 - 8  # Karen keeps 10 cookies for herself and gives 8 to her grandparents

    # Calculate the number of cookies each classmate will receive
    cookies_per_person = remaining_cookies // 16  # use integer division since we can't give out a fraction of a cookie
    result = cookies_per_person
    return result

print(solution())