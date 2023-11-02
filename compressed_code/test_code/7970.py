def solution():
    
    stores_2018 = 23
    new_stores_2019 = 5
    closed_stores_2019 = 2
    new_stores_2020 = 10
    closed_stores_2020 = 6
    
    stores_2019 = stores_2018 + new_stores_2019 - closed_stores_2019
    stores_2020 = stores_2019 + new_stores_2020 - closed_stores_2020
    
    result = stores_2020
    return result

print(solution())