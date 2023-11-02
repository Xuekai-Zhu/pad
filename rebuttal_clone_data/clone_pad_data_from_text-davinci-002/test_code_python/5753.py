def solution():
     total_people = 55
     boys = 30
     girls = total_people - boys
     long_hair = 3/5
     girls_with_long_hair = long_hair * girls
     girls_with_short_hair = girls - girls_with_long_hair
     result = girls_with_short_hair
     return result

print(solution())