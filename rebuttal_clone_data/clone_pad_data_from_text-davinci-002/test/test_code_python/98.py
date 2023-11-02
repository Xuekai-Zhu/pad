def solution():
    
    height_2017 = 100
    height_2018 = height_2017 + (height_2017 * 0.1)
    height_2019 = height_2018 + (height_2018 * 0.1)
    total_growth = height_2019 - height_2017
    result = total_growth
    return result

print(solution())