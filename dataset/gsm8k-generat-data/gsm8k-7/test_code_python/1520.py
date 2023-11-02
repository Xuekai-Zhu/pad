def solution():
    total_cookies = 30
    father_cookies = 10
    mother_cookies = father_cookies / 2
    brother_cookies = mother_cookies + 2

    # Calculate the total number of cookies eaten by the family
    family_cookies = father_cookies + mother_cookies + brother_cookies

    # Calculate the number of cookies left for Monica
    monica_cookies = total_cookies - family_cookies
    result = monica_cookies
    return result

print(solution())