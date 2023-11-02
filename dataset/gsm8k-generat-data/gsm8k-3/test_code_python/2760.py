def solution():
    """Joel is 5 years old and his dad is 32 years old.  How old will Joel be when his dad is twice as old as him?"""
    # Define Joel's age and his dad's age
    joel_age = 5
    dad_age = 32

    # Define the difference in age between Joel and his dad
    age_difference = dad_age - joel_age

    # Find the age at which his dad will be twice as old as him
    twice_as_old_age = dad_age + age_difference

    # Calculate how many years it will take for his dad to be twice as old as him
    years_until_twice_as_old = twice_as_old_age - joel_age

    # Calculate the age Joel will be when his dad is twice as old as him
    joel_age_at_twice_as_old = joel_age + years_until_twice_as_old

    # Display the age Joel will be
    result = joel_age_at_twice_as_old
    return result

print(solution())