def solution():
     cookies_start = 0
     cookies_eaten = 3
     cookies_given = 5
     cookies_ taken = 1 + 3 + 5 + 7 + 9
     cookies_left = cookies_start - cookies_eaten - cookies_given - cookies_taken
     result = cookies_left
     return result

print(solution())