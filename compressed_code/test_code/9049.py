def solution():
    
    total_teeth = 32
    person1_removed = total_teeth * (1/4)
    person2_removed = total_teeth * (3/8)
    person3_removed = total_teeth * (1/2)
    person4_removed = 4
    total_removed = person1_removed + person2_removed + person3_removed + person4_removed
    result = total_removed
    return result

print(solution())