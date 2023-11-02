def solution():
    
    # Define the age of the brothers and sisters
    brothers_age = 12
    sisters_age = 3 * brothers_age

    # Calculate the age of the older brother
    older_brother_age = brothers_age / 2

    # Calculate the total age of all the siblings
    total_age = brothers_age + sisters_age + older_brother_age

    # Display the total age
    result = total_age
    return result

print(solution())