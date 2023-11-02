def solution():
    
    initial_people = 40
    initial_cans = 600
    reduced_people = int(initial_people * 0.7)  
    reduced_cans = (initial_cans * reduced_people) / initial_people
    result = reduced_cans
    return result

print(solution())