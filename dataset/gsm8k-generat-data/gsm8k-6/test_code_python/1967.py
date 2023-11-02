def solution():
    # Calculate the number of hot dogs Guise ate on Tuesday and Wednesday
    Tuesday_dogs = 10 + 2  # Guise ate two more hot dogs on Tuesday than on Monday
    Wednesday_dogs = Tuesday_dogs + 2  # Guise ate two more hot dogs on Wednesday than on Tuesday
    total_dogs = 10 + Tuesday_dogs + Wednesday_dogs  # total number of hot dogs Guise ate by Wednesday
    result = total_dogs
    return result

print(solution())