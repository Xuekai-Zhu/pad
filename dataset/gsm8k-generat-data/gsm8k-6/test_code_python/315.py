def solution():
    # Calculate the total amount of provisions in the castle
    total_provisions = 300 * 90  # enough provisions to feed 300 people for 90 days

    # Calculate the amount of provisions consumed in 30 days
    provisions_consumed = 300 * 30  # provisions consumed by 300 people in 30 days

    # Calculate the amount of provisions remaining after 30 days
    provisions_remaining = total_provisions - provisions_consumed

    # Calculate the number of people remaining in the castle
    people_remaining = 300 - 100  # 100 people leave the castle

    # Calculate the number of days remaining until all the food runs out
    days_remaining = provisions_remaining / (people_remaining * 3)

    result = days_remaining
    return result

print(solution())