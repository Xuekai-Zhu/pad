def solution():
    """Peggy has 6 dolls. Her grandmother gives Peggy her own collection of 30 dolls. Over the year, Peggy receives half that amount of dolls between her birthday and Christmas. How many dolls does Peggy now have?"""
    # Define the initial number of dolls
    initial_dolls = 6

    # Define the number of dolls given by the grandmother
    grandmother_dolls = 30

    # Calculate the number of dolls received between birthday and Christmas
    bday_christmas_dolls = grandmother_dolls / 2

    # Calculate the total number of dolls Peggy has now
    total_dolls = initial_dolls + grandmother_dolls + bday_christmas_dolls

    result = total_dolls
    return result

print(solution())