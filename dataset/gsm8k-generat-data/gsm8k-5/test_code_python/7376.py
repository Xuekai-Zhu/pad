def solution():
    total_jerky = 40  # Janette brought 40 pieces of beef jerky
    daily_jerky = 1 + 1 + 2  # Janette wants to eat 1 for breakfast, 1 for lunch, and 2 for dinner each day
    jerky_for_trip = daily_jerky * 5  # Janette is camping for 5 days and wants to eat a certain amount of jerky each day

    # Calculate the remaining jerky after the trip
    remaining_jerky = total_jerky - jerky_for_trip
    jerky_for_brother = remaining_jerky / 2  # Janette plans on giving half of the remaining pieces to her brother

    # Calculate the final number of pieces of jerky Janette will have left after giving some to her brother
    final_jerky = remaining_jerky - jerky_for_brother
    result = final_jerky
    return result

print(solution())