def solution():
    katherine_time = 20  # Katherine takes 20 hours to develop a website
    naomi_time = katherine_time * (5/4)  # Naomi takes 1/4 more time than Katherine

    # Calculate the total time Naomi takes to develop the 30 websites
    total_naomi_time = naomi_time * 30

    result = total_naomi_time
    return result

print(solution())