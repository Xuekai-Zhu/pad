def solution():
    """On a particular day, Rose's teacher read the register and realized there were twice as many girls as boys present on that day. The class has 250 students, and all the 140 girls were present. If all the absent students were boys, how many boys were absent that day?"""
    total_students = 250
    present_girls = 140
    present_boys = total_students - present_girls
    
    # Since there were twice as many present girls as boys, we can find the number of present boys by dividing present girls by 2
    present_boys_calculated = present_girls / 2
    
    # The difference between the total number of boys and present boys gives the number of absent boys
    absent_boys = present_boys_calculated - present_boys
    result = absent_boys
    
    return result

print(solution())