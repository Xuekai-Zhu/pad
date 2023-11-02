def solution():
    """There are enough provisions in a castle to feed 300 people for 90 days. After 30 days, 100 people leave the castle. How many more days are left until all the food runs out?"""
    # Calculate the total amount of provisions
    total_provisions = 300 * 90

    # Calculate the amount of provisions used in the first 30 days
    provisions_used = 300 * 30

    # Calculate the amount of provisions remaining after 30 days
    remaining_provisions = total_provisions - provisions_used

    # Calculate the number of people remaining
    remaining_people = 300 - 100

    # Calculate the amount of provisions used per person per day
    provisions_per_person_per_day = remaining_provisions / (remaining_people * 60)

    # Calculate the number of days until all the food runs out
    days_remaining = remaining_provisions / (remaining_people * provisions_per_person_per_day)

    # Display the number of days remaining
    result = days_remaining
    return result

print(solution())