def solution():
     cookies = 19
     cookies_given_to_friend = 5
     cookies_given_to_family = (cookies - cookies_given_to_friend) / 2
     cookies_eaten = 2
     cookies_left = cookies - cookies_given_to_friend - cookies_given_to_family - cookies_eaten
     result = cookies_left
     return result

print(solution())