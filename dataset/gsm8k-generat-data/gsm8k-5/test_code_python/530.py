def solution():
    total_cookies = 42
    total_candy = 63
    total_brownies = 21
    total_desserts = total_cookies + total_candy + total_brownies
    total_people = 7

    # Calculate the number of desserts each person will get
    desserts_per_person = total_desserts // total_people
    result = desserts_per_person
    return result

print(solution())