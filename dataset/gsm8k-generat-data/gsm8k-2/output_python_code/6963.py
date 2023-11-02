def solution():
    """James binges on Cheezits and eats 3 bags that are 2 ounces each. There are 150 calories in an ounce of Cheezits. He then goes for a 40-minute run and burns 12 calories per minute. How many excess calories did he eat?"""
    cheezit_size = 2 # in ounces
    cheezit_calories = 150 # per ounce
    num_bags = 3
    total_cheezit_calories = cheezit_size * cheezit_calories * num_bags
    run_time = 40 # in minutes
    calories_burnt_per_minute = 12
    total_calories_burnt = run_time * calories_burnt_per_minute
    excess_calories = total_cheezit_calories - total_calories_burnt
    result = excess_calories
    return result

print(solution())