def solution():
    cookies = 42
    candy = 63
    brownies = 21
    people = 7
    cookies_per_person = cookies / people
    candy_per_person = candy / people
    brownies_per_person = brownies / people
    result = (cookies_per_person, candy_per_person, brownies_per_person)
    
    return result

print(solution())