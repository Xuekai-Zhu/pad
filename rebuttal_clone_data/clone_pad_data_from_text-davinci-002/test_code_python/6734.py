def solution():
 cookies_baked = 120
 cookies_sold_morning = 36
 cookies_sold_lunch = 57
 cookies_sold_afternoon = 16
 cookies_left = cookies_baked - cookies_sold_morning - cookies_sold_lunch - cookies_sold_afternoon
 result = cookies_left
 return result

print(solution())