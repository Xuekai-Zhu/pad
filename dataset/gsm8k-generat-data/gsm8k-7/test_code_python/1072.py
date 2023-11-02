def solution():
    num_shirts_each_type = 200
    
    num_buttons_3 = 3
    num_buttons_5 = 5
    
    # Calculate the total number of buttons for all 200 shirts with 3 buttons
    total_buttons_3 = num_shirts_each_type * num_buttons_3
    
    # Calculate the total number of buttons for all 200 shirts with 5 buttons
    total_buttons_5 = num_shirts_each_type * num_buttons_5
    
    # Calculate the total number of buttons for all shirts
    total_buttons = total_buttons_3 + total_buttons_5
    result = total_buttons
    return result

print(solution())