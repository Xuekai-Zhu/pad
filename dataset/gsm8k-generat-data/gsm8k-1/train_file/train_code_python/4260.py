def solution():
    """There are 30 students in Ms. Leech's class. Twice as many girls as boys are in the class. There are 10 boys in the class and each boy today brought 5 cups for science activity class as Ms. Leech had instructed. If the total number of cups brought by the students in the class is 90, how many cups did each girl bring?"""
    
    # Calculate number of girls in the class
    boys_in_class = 10
    girls_in_class = 2 * boys_in_class
    
    # Calculate total number of cups brought by boys
    cups_per_boy = 5
    total_cups_by_boys = cups_per_boy * boys_in_class
    
    # Calculate total number of cups brought by the class (boys and girls)
    total_cups = 90
    total_cups_by_girls = total_cups - total_cups_by_boys
    
    # Calculate number of cups brought by each girl
    cups_per_girl = total_cups_by_girls / girls_in_class
    
    result = cups_per_girl
    return result

print(solution())