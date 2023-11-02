def solution():
    """Jean is a customer service rep and answered 35 phone calls on Monday. On Tuesday, she answered 46 and took 27 calls on Wednesday. On Thursday she answered 61 calls and finished off answering 31 calls on Friday. What’s the average number of calls she answers per day?"""
    # Define the total number of calls and the number of days worked
    total_calls = 35 + 46 + 27 + 61 + 31
    num_days_worked = 5

    # Calculate the average number of calls per day
    average_calls_per_day = total_calls / num_days_worked

    # return the result
    result = average_calls_per_day
    return result

print(solution())