def solution():
    total_slices = 16
    leftover_slices = 4
    slices_per_person = 2
    
    # Calculate the number of slices eaten by Alyana and her friends
    eaten_slices = total_slices - leftover_slices
    
    # Calculate the number of people who ate the pizza
    num_people = eaten_slices / slices_per_person
    
    result = num_people
    return result

print(solution())