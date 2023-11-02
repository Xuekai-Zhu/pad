def solution():
    # Calculate the number of calories in the carrots and broccoli eaten by Tom
    calories_carrots = 51 * 1  # Tom eats 1 pound of carrots
    calories_broccoli = (1/3) * 51 * 2  # Tom eats twice as much broccoli as carrots, and broccoli has 1/3 the calories of carrots
    total_calories = calories_carrots + calories_broccoli  # Total calories consumed by Tom
    result = total_calories
    return result

print(solution())