def solution():
    """John assembles widgets at a factory. He can make 20 widgets an hour and works for 8 hours a day 5 days a week. How many widgets does he make a week?"""
    # Calculate the number of hours John works in a week
    weekly_hours = 8 * 5

    # Calculate the number of widgets John can make in a week
    widgets_per_hour = 20
    widgets_per_week = weekly_hours * widgets_per_hour

    # Return the result
    result = widgets_per_week
    return result

print(solution())