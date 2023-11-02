def solution():
    yellow_plants = 10
    purple_plants = yellow_plants * 1.8
    total_plants = yellow_plants + purple_plants
    green_plants = total_plants * 0.25
    total_flowers = yellow_plants + purple_plants + green_plants
    result = total_flowers
    return result

print(solution())