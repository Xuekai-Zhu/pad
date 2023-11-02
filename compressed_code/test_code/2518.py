def solution():
    
    total_pancakes = 12
    total_people = 8
    current_pancakes_per_person = total_pancakes / total_people
    remaining_pancakes_needed = (current_pancakes_per_person * 2 - 1) * total_people - total_pancakes
    result = remaining_pancakes_needed
    return result

print(solution())