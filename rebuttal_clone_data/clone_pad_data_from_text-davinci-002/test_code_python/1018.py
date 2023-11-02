def solution():
    couples = 3
    single_people = 5
    Ron = 1
    
    people = couples * 2 + single_people + Ron
    weeks = people * 52
    result = weeks / people
    return result

print(solution())