def solution():
    
    initial_chocolates = 20
    total_people = 6
    chocolates_per_person = initial_chocolates / total_people
    father_chocolates_received = 0.5 * chocolates_per_person * total_people
    total_chocolates_after_father_received = initial_chocolates - father_chocolates_received
    total_chocolates_after_father_gave_to_mother = total_chocolates_after_father_received - 3
    total_chocolates_after_father_ate = total_chocolates_after_father_gave_to_mother - 2
    result = total_chocolates_after_father_ate
    return result

print(solution())