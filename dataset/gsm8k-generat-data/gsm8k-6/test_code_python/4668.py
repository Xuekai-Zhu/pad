def solution():
    # Calculate the total number of homework hours Paul has to do
    total_homework_hours = 2 * 5 + 5  # 2 hours of homework on weeknights for 5 nights + 5 hours for the weekend

    # Calculate the number of homework hours Paul has to do on the other nights
    remaining_nights = 5 - 2  # Paul has practice on 2 nights, so there are 5 - 2 = 3 remaining weeknights
    remaining_homework_hours = (total_homework_hours - (2 * 2)) / remaining_nights  # Subtract 2 hours for the nights he has practice, then divide by the remaining nights

    result = remaining_homework_hours
    return result

print(solution())