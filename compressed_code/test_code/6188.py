def solution():
    
    total_cookies = 42
    total_candy = 63
    total_brownies = 21
    total_people = 7

    
    total_desserts = total_cookies + total_candy + total_brownies

    
    desserts_per_person = total_desserts / total_people

    result = desserts_per_person
    return result

print(solution())