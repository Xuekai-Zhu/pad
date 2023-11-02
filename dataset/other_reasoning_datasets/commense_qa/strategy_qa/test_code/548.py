def solution():
    women_participants = 4637
    men_participants = 6305
    if women_participants <= men_participants/2: #Assuming that each male athlete has only one potential hookup partner
        result = "yes"
    else:
        result = "no"
    return result

print(solution())