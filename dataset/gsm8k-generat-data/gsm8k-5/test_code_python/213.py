def solution():
    # Calculate the number of tomato seeds planted in the morning
    mike_morning_plants = 50
    ted_morning_plants = 2 * mike_morning_plants
    morning_total = mike_morning_plants + ted_morning_plants

    # Calculate the number of tomato seeds planted in the afternoon
    mike_afternoon_plants = 60
    ted_afternoon_plants = mike_afternoon_plants - 20  # Ted planted 20 fewer seeds than Mike
    afternoon_total = mike_afternoon_plants + ted_afternoon_plants

    # Calculate the total number of tomato seeds planted
    total_plants = morning_total + afternoon_total
    result = total_plants
    return result

print(solution())