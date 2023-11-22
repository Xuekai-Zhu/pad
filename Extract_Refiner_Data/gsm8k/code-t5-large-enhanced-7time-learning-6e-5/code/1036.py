def solution():
    
    # Define the number of letters delivered on Monday
    monday_letters = 425

    # Calculate the number of letters delivered on Tuesday
    tuesday_letters = monday_letters * 1/5

    # Calculate the number of letters delivered on Wednesday
    wednesday_letters = tuesday_letters * 2 + 5

    # Calculate the total number of letters delivered
    total_letters = monday_letters + tuesday_letters + wednesday_letters

    # Display the total number of letters delivered
    result = total_letters
    return result

print(solution())