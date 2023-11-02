def solution():
     total_cookies = 20
     cookies_to_brother = 10
     cookies_to_mother = cookies_to_brother / 2
     cookies_to_sister = (total_cookies - cookies_to_brother - cookies_to_mother) * (2/3)
     cookies_left = total_cookies - cookies_to_brother - cookies_to_sister
     result = cookies_left
     return result

print(solution())