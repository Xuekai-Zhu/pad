def solution():
    miles_to_work = 20 * 2  # John drives 20 miles to work each way
    work_days = 5  # John works 5 days a week
    leisure_miles = 40  # John drives 40 miles a week for leisure travel

    # Calculate the total miles John drives in a week
    total_miles = (miles_to_work * work_days) + leisure_miles

    # Calculate the total gallons of gas John uses in a week
    gallons_used = total_miles / 30  # John's car gets 30 mpg

    result = gallons_used
    return result

print(solution())