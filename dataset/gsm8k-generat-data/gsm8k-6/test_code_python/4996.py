def solution():
    # Calculate the total number of bottles of soda Rebecca bought
    total_bottles = 3 * 6 * 2  # three 6-packs, with each pack having 2 bottles and each bottle is half a bottle of soda
    
    # Calculate the number of bottles of soda Rebecca drinks in four weeks
    bottles_drunk = 7 * 4 * 0.5  # seven days in a week, four weeks, and Rebecca drinks half a bottle a day
    
    # Calculate the remaining bottles of soda after four weeks
    bottles_left = total_bottles - bottles_drunk
    
    result = bottles_left
    return result

print(solution())