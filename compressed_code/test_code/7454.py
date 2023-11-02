def solution():
    
    
    total_volcanoes = 200
    first_two_months = int(total_volcanoes * 0.2)
    remaining_volcanoes = total_volcanoes - first_two_months
    next_six_months = int(remaining_volcanoes * 0.4)
    remaining_volcanoes = remaining_volcanoes - next_six_months
    last_two_months = int(remaining_volcanoes * 0.5)
    intact_volcanoes = remaining_volcanoes - last_two_months
    result = intact_volcanoes
    return result

print(solution())