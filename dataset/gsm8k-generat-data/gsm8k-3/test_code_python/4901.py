def solution():
    """My dog was born when I was 15 years old. Two years from now, my dog will turn 4 years old. How old am I now?"""
    # Calculate the age difference between my dog and me
    dog_age_difference = 4 - 2  # In two years, my dog will be 4 years old
    my_age_difference = dog_age_difference + 15  # My dog is two years younger than me

    # Calculate my current age
    my_current_age = my_age_difference + 2  # Two years have passed since my dog was born

    # Display my current age
    result = my_current_age
    return result

print(solution())