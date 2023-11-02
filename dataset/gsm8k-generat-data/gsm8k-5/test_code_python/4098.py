def solution():
    thermos_size = 20  # The teacher drinks coffee from a 20-ounce thermos
    milk_amount = 0.5  # The teacher pours 1/2 cup of milk into the thermos
    cups_per_thermos = 2  # The teacher fills the thermos twice a day
    days_per_week = 5  # The teacher drinks coffee during the 5-day school week

    # Calculate the total amount of coffee the teacher drinks in a week
    total_coffee = (thermos_size - milk_amount) * cups_per_thermos * days_per_week

    # Calculate the amount of coffee the teacher should now drink, which is 1/4 of the original amount
    reduced_coffee = total_coffee / 4
    result = reduced_coffee
    return result

print(solution())