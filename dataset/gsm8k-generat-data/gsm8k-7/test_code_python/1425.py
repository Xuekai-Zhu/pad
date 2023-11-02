def solution():
    betty_rate = 10
    dora_rate = 8
    betty_break_hours = 2
    total_hours = 5

    # Calculate the total number of cupcakes Betty made before her break
    betty_cupcakes_before = betty_rate * (total_hours - betty_break_hours)

    # Calculate the total number of cupcakes Dora made in the same time
    dora_cupcakes = dora_rate * total_hours

    # Calculate the difference between the number of cupcakes they made
    difference = betty_cupcakes_before - dora_cupcakes
    result = difference
    return result

print(solution())