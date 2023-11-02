def solution():
    burger_calories = 400
    carrot_calories = 20
    num_carrots = 5
    total_carrot_calories = carrot_calories * num_carrots
    desired_total_calories = 750

    # Calculate the total calories from the burger and carrots
    total_burger_and_carrot_calories = burger_calories + total_carrot_calories

    # Calculate the remaining calories needed from cookies
    remaining_calories = desired_total_calories - total_burger_and_carrot_calories

    # Calculate the number of cookies each kid gets
    cookies_per_kid = remaining_calories / 50
    result = cookies_per_kid
    return result

print(solution())