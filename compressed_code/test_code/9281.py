def solution():
    
    jaylen_carrots = 5
    jaylen_cucumbers = 2
    kristin_bell_peppers = 2
    kristin_green_beans = 20
    
    jaylen_bell_peppers = kristin_bell_peppers * 2
    kristin_half_green_beans = (kristin_green_beans / 2) - 3
    jaylen_green_beans = kristin_half_green_beans
    
    total_veggies = jaylen_carrots + jaylen_cucumbers + jaylen_bell_peppers + jaylen_green_beans
    
    result = total_veggies
    return result

print(solution())