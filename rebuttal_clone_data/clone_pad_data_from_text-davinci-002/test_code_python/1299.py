def solution():
    tuesday_weeds = 25
    wednesday_weeds = tuesday_weeds * 3
    thursday_weeds = wednesday_weeds / 5
    friday_weeds = thursday_weeds - 10
    total_weeds = tuesday_weeds + wednesday_weeds + thursday_weeds + friday_weeds
    result = total_weeds
    return result

print(solution())