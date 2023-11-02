def solution():
    
    # Define the amount of potato salad each person will eat
    ADULT_SALAD = 10
    CHILD_SALAD = ADULT_SALAD / 2

    # Define the number of adults and children at the picnic
    num_adults = 20
    num_children = 5

    # Calculate the total amount of potato salad needed
    total_potato_salad = (num_adults * ADULT_SALAD) + (num_children * CHILD_SALAD)

    # Display the total amount of potato salad needed
    result = total_potato_salad
    return result

print(solution())