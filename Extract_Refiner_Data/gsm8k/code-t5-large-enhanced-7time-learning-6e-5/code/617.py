def solution():
    
    # Define the number of sessions and the hours worked per session
    sessions = 6 * 2 * 2
    hours_per_session = sessions * 2

    # Calculate the total hours worked
    total_hours = sessions * hours_per_session

    # Calculate the cost of the physical therapy
    therapy_cost = total_hours * 125

    # return the result
    result = therapy_cost
    return result

print(solution())