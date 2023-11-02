def solution():
    """Mandy researched 42 med schools. She applied to 1/3 of the schools she researched and got into half of the schools where she applied. How many schools was Mandy accepted to?"""
    # Define the number of schools Mandy researched
    researched = 42

    # Calculate the number of schools Mandy applied to
    applied = researched // 3

    # Calculate the number of schools Mandy was accepted to
    accepted = applied // 2

    # Display the number of schools Mandy was accepted to
    result = accepted
    return result

print(solution())