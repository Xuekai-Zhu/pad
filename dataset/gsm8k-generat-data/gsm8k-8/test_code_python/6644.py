def solution():
    # Define Thomas' hours
    thomas_hours = x
    
    # Define Toby's hours in terms of Thomas' hours
    toby_hours = 2 * thomas_hours - 10
    
    # Define Rebecca's hours in terms of Toby's hours
    rebecca_hours = toby_hours - 8
    
    # Calculate the total hours worked
    total_hours = thomas_hours + toby_hours + rebecca_hours
    
    # Use the information that the total hours was 157 to solve
    rebecca_hours = 157 - (thomas_hours + toby_hours)
    
    result = rebecca_hours
    return result

print(solution())