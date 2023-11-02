def solution():
    hans_age = 8
    years_to_add = 4

    # Calculate Hans' age in four years
    hans_future_age = hans_age + years_to_add

    # Calculate Annika's age in four years
    annika_future_age = hans_future_age * 3

    # Calculate Annika's current age
    annika_current_age = annika_future_age - years_to_add
    result = annika_current_age
    return result

print(solution())