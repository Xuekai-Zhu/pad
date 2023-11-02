def solution():
    
    lilacs_sold = 10
    roses_sold = 3 * lilacs_sold
    gardenias_sold = lilacs_sold / 2
    total_flowers_sold = lilacs_sold + roses_sold + gardenias_sold
    result = total_flowers_sold
    return result

print(solution())