def solution():
    # Calculate the total amount of food the puppy will eat over the next 4 weeks
    first_week_food = (1/4)*3*7  # amount of food the puppy will eat in the first week
    second_week_food = (1/2)*2*7  # amount of food the puppy will eat in the second week
    total_food = first_week_food + second_week_food + 1/2  # total amount of food the puppy will eat over 4 weeks, including today's feeding
    result = total_food
    return result

print(solution())