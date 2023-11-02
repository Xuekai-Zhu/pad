def solution():
    loads_of_laundry_per_week = 3
    weeks_in_a_year = 52
    loads_of_laundry_in_a_year = loads_of_laundry_per_week * weeks_in_a_year
    detergent_pods_per_pack = 39
    number_of_packs = loads_of_laundry_in_a_year / detergent_pods_per_pack
    result = number_of_packs
    
    return result

print(solution())