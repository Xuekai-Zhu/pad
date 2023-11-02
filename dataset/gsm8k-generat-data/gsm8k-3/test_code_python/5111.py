def solution():
    """Three siblings are born 5 years apart, each. If the eldest child is 20 years old now, what's the total of the ages of the three siblings 10 years from now?"""
    # Define the age difference between the siblings
    AGE_DIFFERENCE = 5

    # Define the age of the eldest sibling
    eldest_age = 20

    # Calculate the age of the second and third siblings
    second_age = eldest_age - AGE_DIFFERENCE
    third_age = second_age - AGE_DIFFERENCE

    # Calculate the total age of the siblings 10 years from now
    total_age = (eldest_age + 10) + (second_age + 10) + (third_age + 10)

    # Display the total age
    result = total_age
    return result

print(solution())