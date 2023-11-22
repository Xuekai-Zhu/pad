def solution():
    
    # Define the initial plan length and the daily call length
    plan_length = 1000
    daily_call_length = 15

    # Calculate the total call length for the month
    total_call_length = plan_length + (daily_call_length * 30)

    # Add the extra minutes for the boss call
    total_call_length += 300

    # Calculate the remaining plan length
    remaining_plan_length = plan_length - total_call_length

    # return the result
    result = remaining_plan_length
    return result

print(solution())