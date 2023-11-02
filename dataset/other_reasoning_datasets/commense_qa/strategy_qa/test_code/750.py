def solution():
    sugar_per_celery_stick = 1/10 # each serving of celery has 10 sticks
    sugar_per_day = 36 # recommended daily intake of sugar to prevent diabetes
    weight_of_adult_male = 197 # average weight of an adult male
    celery_needed_per_day = sugar_per_day/sugar_per_celery_stick 
    celery_needed_per_year = celery_needed_per_day*365
    celery_needed_to_eat_weight = weight_of_adult_male/sugar_per_celery_stick
    if celery_needed_to_eat_weight >= celery_needed_per_year:
        result = "yes"
    else:
        result = "no"
    return result

print(solution())