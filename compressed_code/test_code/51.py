def solution():
    
    total_oil = 290
    total_cans = 24
    given_cans = 10
    given_cans_oil = given_cans * 8
    remaining_oil = total_oil - given_cans_oil
    remaining_cans = total_cans - given_cans
    oil_per_can = remaining_oil / remaining_cans
    result = oil_per_can
    return result

print(solution())