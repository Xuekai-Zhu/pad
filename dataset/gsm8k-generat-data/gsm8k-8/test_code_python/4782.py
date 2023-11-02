def solution():
    # Define amount of games Neil had at first
    neil_initial_num = 7
    
    # Calculate amount of games Henry has now
    henry_current_num = 4 * neil_initial_num + 6
    
    # Calculate amount of games Henry had at first
    henry_initial_num = henry_current_num - 6
    
    result = henry_initial_num
    return result

print(solution())