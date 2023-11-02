def solution():
    """Joel is 5 years old and his dad is 32 years old. How old will Joel be when his dad is twice as old as him?"""
    # Define Joel's age and his dad's age
    joel_age = 5
    dad_age = 32

    # Define the age difference when dad is twice as old as Joel
    age_difference = dad_age - 2 * joel_age

    # Calculate the number of years until dad is twice as old as Joel
    years = age_difference - dad_age

    # Calculate Joel's age when his dad is twice as old as him
    joel_future_age = joel_age + years

    # return the result
    result = joel_future_age
    return result

print(solution())