def solution():
    
    houses = 5
    gnomes_per_house = 3
    total_gnomes = 20
    gnomes_in_fifth_house = total_gnomes - (houses - 1) * gnomes_per_house
    result = gnomes_in_fifth_house
    return result

print(solution())