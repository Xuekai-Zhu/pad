def solution():
    
    initial_phones = 15
    repaired_phones = 3
    new_phones = 6
    total_phones = initial_phones + new_phones
    remaining_phones = total_phones - repaired_phones
    phones_per_person = remaining_phones / 2
    result = phones_per_person
    return result

print(solution())