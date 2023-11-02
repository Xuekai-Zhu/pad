def solution():
    average_six_year_old_weight = 45
    max_fur_seal_weight = 120
    feeding_habit = "fish"
    physical_traits = ["sharp teeth"]
    if max_fur_seal_weight > average_six_year_old_weight and feeding_habit == "fish" and "sharp teeth" in physical_traits:
        result = "no"
    else:
        result = "yes"
    return result

print(solution())