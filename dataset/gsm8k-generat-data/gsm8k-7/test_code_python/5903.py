def solution():
    num_teas = 6

    # Let's use the variable x to represent the number of lattes sold
    # The coffee shop sold 8 more than four times the number of lattes as it did teas
    # So we can write an equation: 4x + 8 = number of lattes sold + 6
    # Simplifying the equation: 4x = number of lattes sold + 2
    # Since the number of lattes sold must be a whole number, we can solve for x by trial and error
    # Starting with x = 1, we can plug it into the equation and see if the left side equals the right side
    # If it doesn't, we can try the next whole number until we find the correct value

    x = 1
    while True:
        if 4*x == num_teas + 2:
            break
        else:
            x += 1

    num_lattes = 4*x + 8
    result = num_lattes
    return result

print(solution())