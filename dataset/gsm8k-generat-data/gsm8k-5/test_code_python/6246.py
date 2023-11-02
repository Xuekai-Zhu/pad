def solution():
    total_cookies = 600  # There were 600 cookies in the box
    nicole_cookies = (2/5) * total_cookies  # Nicole ate 2/5 of the total number of cookies
    remaining_cookies = total_cookies - nicole_cookies  # Calculate the number of cookies remaining after Nicole ate
    eduardo_cookies = (3/5) * remaining_cookies  # Eduardo ate 3/5 of the remaining amount
    total_eaten_cookies = nicole_cookies + eduardo_cookies  # Calculate the total number of cookies eaten
    percent_remaining = ((total_cookies - total_eaten_cookies) / total_cookies) * 100  # Calculate the percentage of cookies remaining
    result = percent_remaining
    return result

print(solution())