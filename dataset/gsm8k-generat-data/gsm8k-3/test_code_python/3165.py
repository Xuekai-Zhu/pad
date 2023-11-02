def solution():
    """In seven years, Talia will be 20 years old. Talia's mom is currently three times as old as Talia is today. In three years, Talia's father will be the same age as Talia's mom is today. Currently, how many years old is Talia's father?"""
    # Define Talia's current age
    talia_current_age = 13

    # Calculate Talia's mom's current age
    mom_current_age = talia_current_age * 3

    # Calculate Talia's father's current age
    father_current_age = mom_current_age + 3

    # Display Talia's father's current age
    result = father_current_age
    return result

print(solution())