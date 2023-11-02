def solution():
    """Betty and Dora started making some cupcakes at the same time. Betty makes 10 cupcakes every hour and Dora makes 8 every hour. If Betty took a two-hour break, what is the difference between the number of cupcakes they made after 5 hours?"""
    
    # Define the number of cupcakes Betty and Dora make per hour
    betty_cupcakes_per_hour = 10
    dora_cupcakes_per_hour = 8

    # Calculate the number of cupcakes both can make in an hour
    cupcakes_per_hour = betty_cupcakes_per_hour + dora_cupcakes_per_hour

    # Calculate the total number of cupcakes made in the first three hours
    total_cupcakes_first_three_hours = cupcakes_per_hour * 3

    # Calculate the total number of cupcakes Betty makes after the break
    betty_cupcakes_after_break = 10 * 2

    # Calculate the total number of cupcakes both make after 5 hours
    total_cupcakes_after_5_hours = total_cupcakes_first_three_hours + betty_cupcakes_after_break + (cupcakes_per_hour * 2)

    # Calculate the difference in the number of cupcakes Betty and Dora make after 5 hours
    cupcakes_difference = abs((betty_cupcakes_per_hour * 3) + betty_cupcakes_after_break - ((dora_cupcakes_per_hour + betty_cupcakes_per_hour) * 5))

    result = cupcakes_difference
    return result

print(solution())