def solution():
    ketchup = 3
    vinegar = 1
    honey = 1
    burgers = 18
    pulled_pork = 18
    sauce_per_burger = 0.25
    sauce_per_pork = 0.166666666666666666
    total_sauce = ketchup + vinegar + honey
    sauce_needed = burgers * sauce_per_burger + pulled_pork * sauce_per_pork
    result = total_sauce / sauce_needed
    
    return result

print(solution())