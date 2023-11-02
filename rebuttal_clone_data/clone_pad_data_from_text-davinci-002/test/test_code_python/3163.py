def solution():
    phones_at_beginning = 15
    phones_repaired = 3
    phones_dropped_off = 6
    phones_remaining = phones_at_beginning - phones_repaired + phones_dropped_off
    coworker_helps = True
    
    if coworker_helps:
        # if the coworker helps, then each person needs to repair half of the remaining phones
        phones_per_person = phones_remaining / 2
    else:
        # if the coworker does not help, then Kevin needs to repair all of the remaining phones
        phones_per_person = phones_remaining
        
    result = phones_per_person
    
    return result

print(solution())