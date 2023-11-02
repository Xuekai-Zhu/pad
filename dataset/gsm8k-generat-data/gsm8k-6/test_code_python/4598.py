def solution():
    # Calculate the total amount spent on white t-shirts
    men_white = 20
    women_white = men_white - 5
    total_white = (men_white + women_white) * 20 # There are 20 employees in each sector
    
    # Calculate the total amount spent on black t-shirts
    men_black = 18
    women_black = men_black - 5
    total_black = (men_black + women_black) * 20 # There are 20 employees in each sector
    
    # Calculate the total amount spent
    total_spent = total_white + total_black
    result = total_spent
    return result

print(solution())