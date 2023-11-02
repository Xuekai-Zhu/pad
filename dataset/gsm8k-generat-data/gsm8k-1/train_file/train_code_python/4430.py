def solution():
    """Jaylen has 5 carrots and 2 cucumbers. Jaylen has twice as many bell peppers as Kristin. Jaylen has 3 less than half as many green beans as Kristin. If Kristin has 2 bell peppers and 20 green beans, how many vegetables does Jaylen have in total?"""
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