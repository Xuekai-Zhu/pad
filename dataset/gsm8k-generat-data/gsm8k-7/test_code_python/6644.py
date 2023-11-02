def solution():
    total_hours = 157
    x = 0 # Thomas' hours
    y = 0 # Toby's hours
    z = 0 # Rebecca's hours

    # Calculate Toby's hours
    y = 2 * x - 10

    # Calculate Rebecca's hours
    z = y - 8

    # Calculate the total of all hours worked
    total_worked = x + y + z

    # Calculate Rebecca's hours by subtracting Thomas and Toby's hours from the total
    rebecca_hours = total_hours - total_worked
    result = rebecca_hours
    return result

print(solution())