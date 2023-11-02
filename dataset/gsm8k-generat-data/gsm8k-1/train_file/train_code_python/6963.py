def solution():
    """James binges on Cheezits and eats 3 bags that are 2 ounces each. There are 150 calories in an ounce of Cheezits. He then goes for a 40-minute run and burns 12 calories per minute. How many excess calories did he eat?"""
    bags_of_cheezits = 3
    ounces_per_bag = 2
    calories_per_ounce = 150
    total_cheezit_calories = bags_of_cheezits * ounces_per_bag * calories_per_ounce
    run_time = 40  # minutes
    calories_burned_per_minute = 12
    total_calories_burned = run_time * calories_burned_per_minute
    excess_calories = total_cheezit_calories - total_calories_burned
    result = excess_calories
    return result

print(solution())