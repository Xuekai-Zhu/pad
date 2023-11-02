def solution():
    total_shampoo = 10
    hot_sauce_added = 0.5 * 4
    shampoo_used = 1 * 4
    hot_sauce_percentage = (hot_sauce_added / (total_shampoo - shampoo_used + hot_sauce_added)) * 100
    result = hot_sauce_percentage
    return result

print(solution())