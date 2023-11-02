def solution():
    """Selena and Josh were running in a race. Together they ran 36 miles. Josh ran half of the distance that Selena ran. How many miles did Selena run?"""
    total_distance = 36
    josh_distance = total_distance / 3
    selena_distance = total_distance - josh_distance
    result = selena_distance
    return result

print(solution())