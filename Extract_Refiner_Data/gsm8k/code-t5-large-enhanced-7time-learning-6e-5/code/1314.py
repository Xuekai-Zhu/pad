def solution():
    
    # Define the number of people and the number of pizzas
    num_people = 4
    num_pizzas = 7

    # Calculate the total number of slices
    total_slices = num_pizzas * 8

    # Calculate the number of slices each person can have
    slices_per_person = total_slices // num_people

    # Display the number of slices each person can have
    result = slices_per_person
    return result

print(solution())