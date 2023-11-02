def solution():
    
    # Define the phone plan time and the number of days in a month
    PHONE_TIME = 1000
    DAYS_IN_MONTH = 30

    # Calculate the total call time for the month
    total_call_time = PHONE_TIME * DAYS_IN_MONTH

    # Add the extra minutes Jason's boss call
    total_call_time += 15

    # Add the extra minutes Jason's boss call
    total_call_time += 300

    # Calculate the remaining call time
    remaining_call_time = total_call_time - total_call_time

    # Display the remaining call time
    result = remaining_call_time
    return result

print(solution())