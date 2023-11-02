def solution():
    num_carrots_tuesday = 4
    num_carrots_wednesday = 6
    num_carrots_total = 15
    
    # Calculate the number of carrots Wilfred needs to eat on Thursday
    num_carrots_thursday = num_carrots_total - num_carrots_tuesday - num_carrots_wednesday
    
    result = num_carrots_thursday
    return result

print(solution())