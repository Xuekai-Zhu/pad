def solution():
    
    # Define the length of each lunch and break in minutes
    lunch_length = 30
    break_length = 2 * 15

    # Calculate the total length of Bobby's lunches and breaks in 5 days
    total_length = (lunch_length + break_length) * 5

    # Convert the total length to hours
    total_hours = total_length / 60

    # return the result
    result = total_hours
    return result

print(solution())