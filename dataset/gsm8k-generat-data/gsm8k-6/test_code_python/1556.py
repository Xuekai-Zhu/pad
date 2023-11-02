def solution():
    # Calculate the total number of slices eaten by Alyana and her friends
    total_slices_eaten = 16 - 4  # 16 slices were originally cut and 4 slices are left
    slices_per_person = 2
    # Calculate the number of people who ate the pizza
    num_people = total_slices_eaten // slices_per_person
    result = num_people
    return result

print(solution())