def solution():
    # Calculate the total number of miles John drives in a week
    total_miles = (20 * 2 * 5) + 40  # 20 miles to work each way, 5 days a week, plus 40 miles for leisure travel

    # Calculate the total gallons of gas John uses in a week
    gallons_used = total_miles / 30  # John's car gets 30 mpg
    result = gallons_used
    return result

print(solution())