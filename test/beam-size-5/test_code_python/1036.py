def solution():
    
    # Define the number of letters delivered on Monday
    monday_letters = 425

    # Calculate the number of letters delivered on Tuesday
    tuesday_letters = monday_letters * 1/5

    # Calculate the number of letters delivered on Wednesday
    wednesday_letters = 2 * tuesday_letters + 5

    # Display the number of letters delivered on Wednesday
    result = wednesday_letters
    return result

print(solution())