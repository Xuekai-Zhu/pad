def solution():
    """Mandy researched 42 med schools. She applied to 1/3 of the schools she researched and got into half of the schools where she applied. How many schools was Mandy accepted to?"""
    # Define the total number of schools researched
    total_schools = 42

    # Calculate the number of schools Mandy applied to
    applied_schools = total_schools / 3

    # Calculate the number of schools Mandy was accepted to
    accepted_schools = applied_schools / 2

    # Return the result
    result = accepted_schools
    return result

print(solution())