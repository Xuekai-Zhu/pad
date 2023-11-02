def solution():
    """A factory produces 90 refrigerators per hour. It also produces 70 more coolers than refrigerators per hour. How many products did the factory produce for 5 days if it works 9 hours a day?"""
    # Define the production rates per hour
    refrigerators_per_hour = 90
    coolers_per_hour = refrigerators_per_hour + 70

    # Calculate the total production per day
    production_per_day = (refrigerators_per_hour + coolers_per_hour) * 9

    # Calculate the total production for 5 days
    production_for_5_days = production_per_day * 5

    # return the result
    result = production_for_5_days
    return result

print(solution())