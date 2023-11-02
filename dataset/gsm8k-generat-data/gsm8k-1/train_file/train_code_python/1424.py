def solution():
    """Betty and Dora started making some cupcakes at the same time. Betty makes 10 cupcakes every hour and Dora makes 8 every hour. If Betty took a two-hour break, what is the difference between the number of cupcakes they made after 5 hours?"""
    betty_cupcakes_per_hour = 10
    dora_cupcakes_per_hour = 8
    betty_hours_worked = 3
    dora_hours_worked = 5
    betty_cupcakes_made = betty_cupcakes_per_hour * betty_hours_worked
    dora_cupcakes_made = dora_cupcakes_per_hour * dora_hours_worked
    total_cupcakes_made = betty_cupcakes_made + dora_cupcakes_made
    result = total_cupcakes_made
    return result

print(solution())