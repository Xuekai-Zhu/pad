def solution():
    hot_sauce_added_per_day = 0.5
    shampoo_used_per_day = 1
    days = 4
    hot_sauce_added_totally = hot_sauce_added_per_day * days
    shampoo_used_totally = shampoo_used_per_day * days
    liquid_left = 10 - shampoo_used_totally
    percent_hot_sauce = (hot_sauce_added_totally / (liquid_left + hot_sauce_added_totally)) * 100
    result = percent_hot_sauce
    return result

print(solution())