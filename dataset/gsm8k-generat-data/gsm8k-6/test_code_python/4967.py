def solution():
    # Calculate the total amount of water lost during the first 5 hours
    lost_during_first_5_hours = 32000 * 5  # tank loses 32,000 gallons/hour for 5 hours

    # Calculate the total amount of water lost during the next 10 hours
    lost_during_next_10_hours = 10000 * 10  # tank loses 10,000 gallons/hour for 10 hours

    # Calculate the total amount of water added in the second attempt
    added_in_second_attempt = 40000 * 3  # tank is filled with 40,000 gallons/hour for 3 hours

    # Calculate the total amount of water missing to reach maximum capacity
    missing_gallons = 350000 - (lost_during_first_5_hours + lost_during_next_10_hours + added_in_second_attempt)

    result = missing_gallons
    return result

print(solution())