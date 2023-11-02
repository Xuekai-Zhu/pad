def solution():
    """In 2021, Wayne is 37 years old. His brother Peter is 3 years older than him and their sister Julia is 2 years older than Peter. What year was Julia born in?"""
    # Calculate the birth year of Wayne
    wayne_birthyear = 2021 - 37

    # Calculate the birth year of Peter
    peter_birthyear = wayne_birthyear

    # Calculate the birth year of Julia
    julia_birthyear = peter_birthyear - 2 - 3

    # Display the year Julia was born in
    result = julia_birthyear
    return result

print(solution())