def solution():
    
    total_houses = 5
    gnomes_per_house = 3
    total_gnomes = 20
    gnomes_in_fifth_house = total_gnomes - (gnomes_per_house * (total_houses - 1))
    result = gnomes_in_fifth_house
    return result

print(solution())