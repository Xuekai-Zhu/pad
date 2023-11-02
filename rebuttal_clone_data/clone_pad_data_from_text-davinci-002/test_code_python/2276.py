def solution():
    quarts_of_juice = 6
    reduction_ratio = 1/12
    original_volume = quarts_of_juice * 4
    reduced_volume = original_volume * reduction_ratio
    cups_of_sugar = 1
    final_volume = reduced_volume + cups_of_sugar
    result = final_volume
    return result

print(solution())