def solution():
    # Calculate the total time it took to make the cakes on the day when oven failed
    total_time = 1 + 3 + 1*12  # 1 hour to assemble ingredients, 3 hours for baking (1.5*2), 12 hours for decorating 12 cakes (1*12)
    result = total_time
    return result

print(solution())