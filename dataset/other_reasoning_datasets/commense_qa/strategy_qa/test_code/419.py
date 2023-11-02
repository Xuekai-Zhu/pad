def solution():
    father_of_social_security = "Franklin D. Roosevelt"
    social_security_year = 1935
    panic_of_1907_year = 1907
    serving_in_white_house = False
    if father_of_social_security == "Franklin D. Roosevelt" and social_security_year > panic_of_1907_year and not serving_in_white_house:
        result = "no"
    else:
        result = "unclear"
    return result

print(solution())