def solution():
    # Define the time it takes to walk each type of dog
    poodle_time = 2
    chihuahua_time = 1
    labrador_time = 3

    # Define the number of dogs walked on each day
    monday_poodles = 4
    monday_chihuahuas = 2
    tuesday_chihuahuas = monday_chihuahuas
    wednesday_labradors = 4

    # Calculate the total time spent walking each type of dog
    total_time_poodles = (monday_poodles + x) * poodle_time
    total_time_chihuahuas = (monday_chihuahuas + tuesday_chihuahuas) * chihuahua_time
    total_time_labradors = wednesday_labradors * labrador_time

    # Calculate the total time spent walking all dogs
    total_time = total_time_poodles + total_time_chihuahuas + total_time_labradors

    # Solve for the number of poodles walked on Tuesday
    x = (32 - total_time) / poodle_time - monday_poodles
    result = x
    return result

print(solution())