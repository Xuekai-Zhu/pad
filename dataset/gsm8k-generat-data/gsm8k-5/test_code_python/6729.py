def solution():
    sugar_per_chocolate_bar = 1.5  # The company needs 1.5 grams of sugar to produce one chocolate bar
    chocolate_bars_per_minute = 36  # The company produces 36 chocolate bars every minute
    time_in_minutes = 2  # The company wants to know how much sugar it will use in 2 minutes

    # Calculate the total amount of sugar used in 2 minutes
    total_sugar_used = sugar_per_chocolate_bar * chocolate_bars_per_minute * time_in_minutes
    result = total_sugar_used
    return result

print(solution())