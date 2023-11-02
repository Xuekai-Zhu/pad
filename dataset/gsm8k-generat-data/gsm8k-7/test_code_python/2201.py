def solution():
    initial_plants = 50
    yesterday_plants = initial_plants + 20
    today_plants = initial_plants * 2

    # Calculate the total number of plants Uncle Welly planted
    total_plants = initial_plants + yesterday_plants + today_plants
    result = total_plants
    return result

print(solution())