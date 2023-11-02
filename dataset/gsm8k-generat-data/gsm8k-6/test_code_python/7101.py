def solution():
    # Calculate the number of pints of ice cream Alice bought on Monday
    monday_pints = 4 * 3  # three times the number of pints bought on Sunday

    # Calculate the number of pints of ice cream Alice bought on Tuesday
    tuesday_pints = monday_pints / 3  # one-third of the number of pints bought on Monday

    # Calculate the number of pints of ice cream Alice had on Wednesday
    wednesday_pints = monday_pints/2 - tuesday_pints/2  # half of the pints bought on Monday, minus half of the pints bought on Tuesday

    result = wednesday_pints
    return result

print(solution())