def solution():
    
    num_people = 12 + 7
    seats_per_person = 1 + 2 + 3
    drinks_per_person = 2
    snacks_per_person = 3
    total_drinks = num_people * seats_per_person * drinks_per_person
    total_snacks = num_people * snacks_per_person * snacks_per_person
    total_spent = total_drinks + total_snacks
    result = total_spent
    return result

print(solution())