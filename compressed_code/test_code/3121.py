def solution():
    
    total_shampoo = 10
    daily_shampoo = 1
    hot_sauce = 0.5
    for i in range(4):
        total_shampoo -= daily_shampoo
        total_shampoo += hot_sauce
    hot_sauce_percentage = (hot_sauce * 4 / total_shampoo) * 100

    result = hot_sauce_percentage
    return result

print(solution())