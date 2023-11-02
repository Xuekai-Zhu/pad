def solution():
    """A cat eats nine sausages in 30 minutes. A dog can eat the same number of sausages
    in 2/3 the amount of time the cat takes. Calculate the average time the two take to eat the sausages."""
    sausages_per_cat = 9
    time_per_cat = 30
    time_per_dog = (2/3) * time_per_cat
    sausages_per_dog = sausages_per_cat
    time_total = time_per_cat + time_per_dog
    sausages_total = sausages_per_cat + sausages_per_dog
    average_time = time_total / 2
    result = average_time
    return result

print(solution())