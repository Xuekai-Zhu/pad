def solution():
    # Calculate the number of bath towels Sanya can wash in 2 hours
    num_towels_washable = 7 * 2
    
    # Calculate the number of days needed to wash all the towels
    num_days = 98 / num_towels_washable
    
    # Round up to the nearest whole number of days
    num_days = math.ceil(num_days)
    
    result = num_days
    return result

print(solution())