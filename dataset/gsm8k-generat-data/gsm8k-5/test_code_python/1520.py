def solution():
    total_cookies = 30  # Monica made 30 cookies in total
    father_cookies = 10  # Father ate 10 cookies
    mother_cookies = father_cookies / 2  # Mother ate half as much as the father
    brother_cookies = mother_cookies + 2  # Brother ate 2 more than mother
    remaining_cookies = total_cookies - (father_cookies + mother_cookies + brother_cookies)  # Calculate the number of remaining cookies for Monica
    result = remaining_cookies
    return result

print(solution())