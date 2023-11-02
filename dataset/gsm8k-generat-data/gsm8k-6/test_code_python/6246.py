def solution():
    total_cookies = 600  # total number of cookies
    nicole_cookies = (2/5)*total_cookies  # number of cookies eaten by Nicole
    remaining_cookies = total_cookies - nicole_cookies  # number of cookies remaining
    eduardo_cookies = (3/5)*remaining_cookies  # number of cookies eaten by Eduardo
    remaining_percentage = (remaining_cookies/total_cookies)*100  # percentage of cookies remaining
    result = remaining_percentage
    return result

print(solution())