def solution():
    """In seven years, Talia will be 20 years old.  Talia's mom is currently three times as old as Talia is today.  In three years, Talia's father will be the same age as Talia's mom is today.  Currently, how many years old is Talia's father?"""
    # Set up the age variables
    talia_age = None
    mom_age = None
    dad_age = None

    # Set up the equations based on the given information
    talia_age + 7 = 20
    mom_age = 3 * talia_age
    dad_age + 3 = mom_age

    # Solve for Talia's age
    talia_age = 20 - 7

    # Solve for mom's age
    mom_age = 3 * talia_age

    # Solve for dad's age
    dad_age = mom_age - 3

    # Return dad's age
    result = dad_age
    return result

print(solution())