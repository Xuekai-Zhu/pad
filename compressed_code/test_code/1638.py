def solution():
    
    total_volcanoes = 200
    first_two_months = total_volcanoes * 0.2
    remaining_volcanoes = total_volcanoes - first_two_months
    half_year = remaining_volcanoes * 0.4
    remaining_volcanoes -= half_year
    end_of_year = remaining_volcanoes * 0.5
    intact_volcanoes = remaining_volcanoes - end_of_year
    result = intact_volcanoes
    return result

print(solution())