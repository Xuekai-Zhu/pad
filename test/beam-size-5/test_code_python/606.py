def solution():
    
    monica_street_length = 150
    lewis_street_length = 490
    monica_street_cost = 198
    lewis_street_cost = (lewis_street_length - monica_street_length) * monica_street_cost
    difference = lewis_street_cost - monica_street_cost
    result = difference
    return result

print(solution())