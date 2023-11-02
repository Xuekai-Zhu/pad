def solution():
    num_pancakes = 6
    pancake_calories = 120

    num_bacon = 2
    bacon_calories = 100

    cereal_calories = 200

    # Calculate the total calories from pancakes
    pancake_calories_total = num_pancakes * pancake_calories

    # Calculate the total calories from bacon
    bacon_calories_total = num_bacon * bacon_calories

    # Calculate the total calories from cereal
    cereal_calories_total = cereal_calories

    # Calculate the total calories in the breakfast
    total_calories = pancake_calories_total + bacon_calories_total + cereal_calories_total
    result = total_calories
    return result

print(solution())