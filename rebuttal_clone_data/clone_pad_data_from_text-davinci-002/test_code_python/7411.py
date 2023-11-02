def solution(): 
    tree_height = 180
    percent_increase = 50
    increase_amount = tree_height * (percent_increase/100)
    initial_height = tree_height - increase_amount
    initial_height_in_feet = initial_height/12
    result = initial_height_in_feet
    return result

print(solution())