def solution():
    """Agnes is 25 years old and her daughter, Jane is 6 years old. In how many years will Agnes be twice as old as Jane?"""
    # Initialize years variable
    years = 0

    # While loop to calculate years until Agnes is twice as old as Jane
    while True:
        years += 1
        agnes_age = 25 + years
        jane_age = 6 + years
        if agnes_age == 2 * jane_age:
            break

    # Display the number of years
    result = years
    return result

print(solution())