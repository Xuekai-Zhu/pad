def solution():
    """Lydia has 80 plants. 40% of her plants are flowering plants. Lydia wants to place a fourth of her flowering plants on the porch. If each flowering plant produces 5 flowers, how many flowers are there in total on the porch?"""
    total_plants = 80
    percent_flowering = 40
    flowering_plants = total_plants * (percent_flowering / 100)
    porch_plants = flowering_plants / 4
    flowers_per_plant = 5
    total_flowers = porch_plants * flowers_per_plant
    result = total_flowers
    return result

print(solution())