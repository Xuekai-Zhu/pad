def solution():
    
    lineman_drink = 8
    skill_drink = 6
    num_linemen = 12
    num_skill = 10
    total_water = 126

    
    linemen_water = num_linemen * lineman_drink

    
    skill_water = num_skill * skill_drink

    
    remaining_water = total_water - linemen_water

    
    num_skill_drinks = int(remaining_water / skill_drink)

    
    num_waiting_skill = num_skill - num_skill_drinks

    result = num_waiting_skill
    return result

print(solution())