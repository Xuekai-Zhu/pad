def solution():
    rice = 10  # kilograms of rice
    cooked_in_morning = (9/10) * rice  # kilograms of rice cooked in the morning
    remaining_rice = rice - cooked_in_morning  # remaining rice after cooking in the morning
    cooked_in_evening = (1/4) * remaining_rice  # rice cooked in the evening
    remaining_rice = (remaining_rice - cooked_in_evening) * 1000  # remaining rice in grams
    result = remaining_rice
    return result

print(solution())