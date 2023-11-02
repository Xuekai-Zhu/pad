def solution():
     dollars_in_cookie_jar = 21
     dollars_spent_by_doris = 6
     dollars_spent_by_martha = dollars_spent_by_doris / 2
     dollars_left_in_cookie_jar = dollars_in_cookie_jar - dollars_spent_by_doris - dollars_spent_by_martha
     result = dollars_left_in_cookie_jar
     return result

print(solution())