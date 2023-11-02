def solution():
    total_students = 150
    percent_girls = 60
    girls = total_students * (percent_girls / 100)
    boys = total_students - girls
    boys_in_club =  boys / 3
    boys_not_in_club = boys - boys_in_club
    result = boys_not_in_club
    
    return result

print(solution())