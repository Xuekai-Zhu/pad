def solution():
    # Calculate the ratio of lemonade to total drink volume
    lemonade_ratio = 1.25 / (1.25 + 0.25)  

    # Calculate the total volume of lemonade in the pitcher
    total_lemonade = lemonade_ratio * 18   
    result = total_lemonade
    return result

print(solution())