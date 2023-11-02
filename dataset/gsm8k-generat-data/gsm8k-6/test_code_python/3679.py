def solution():
    # Calculate the amount Macey still needs to save
    remaining_amount = 3 - 1.5  # Macey was able to save $1.5 already

    # Calculate the number of weeks needed to save the remaining amount
    weeks_to_save = remaining_amount / 0.5  # Macey saves $0.50 per week

    result = weeks_to_save
    return result

print(solution())