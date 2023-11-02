def solution():
    
    cases_of_water = 2
    bottles_per_case = 24
    total_bottles = cases_of_water * bottles_per_case
    total_guests = 70
    bottles_per_guest = 2
    total_bottles_needed = total_guests * bottles_per_guest
    additional_bottles_needed = total_bottles_needed - total_bottles
    result = additional_bottles_needed
    return result

print(solution())