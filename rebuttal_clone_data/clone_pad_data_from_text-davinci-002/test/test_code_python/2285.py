def solution():
     total_scientists = 70
     european_scientists = total_scientists / 2
     canadian_scientists = total_scientists / 5
     usa_scientists = total_scientists - european_scientists - canadian_scientists
     result = usa_scientists
     return result

print(solution())