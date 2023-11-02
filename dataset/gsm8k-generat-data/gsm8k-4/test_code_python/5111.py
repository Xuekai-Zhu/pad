def solution():
    """Three siblings are born 5 years apart, each. If the eldest child is 20 years old now, what's the total of the ages of the three siblings 10 years from now?"""
    # Define the current age of the eldest child
    eldest_age = 20

    # Calculate the age of the second child
    second_age = eldest_age - 5

    # Calculate the age of the third child
    third_age = second_age - 5

    # Calculate the total age of the three siblings 10 years from now
    total_age = (eldest_age + 10) + (second_age + 10) + (third_age + 10)

    # return the result
    result = total_age
    return result

print(solution())