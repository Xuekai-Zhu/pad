def solution():
    """The sum of the ages of three boys is 29. If two of the boys are the same age and the third boy is 11 years old, how old are the other two boys?"""
    # Define the age of the third boy
    third_boy_age = 11

    # Calculate the total age of the two other boys
    total_age = 29 - third_boy_age

    # Since two of the boys are the same age, divide the total age by 2 to get their age
    other_boys_age = total_age / 2

    result = int(other_boys_age)
    return result

print(solution())