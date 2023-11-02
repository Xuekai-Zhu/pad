def solution():
    
    choir_members = 52
    boys_percent = 50
    girls_percent = 50
    female_members = choir_members * (boys_percent / 100)
    total_people = choir_members - female_members
    performance_people = total_people / 2
    result = performance_people
    return result

print(solution())