def solution():
    # Subtract the cookies Karen kept and gave away from the total
    cookies_left = 50 - 10 - 8

    # Divide the remaining cookies evenly among the people in her class
    cookies_per_person = cookies_left / 16
    result = cookies_per_person
    return result

print(solution())