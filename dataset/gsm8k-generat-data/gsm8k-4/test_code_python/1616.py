def solution():
    """It’s exam season and Tristan has several exams to prepare for. On Monday, he studies for 4 hours then studies for twice this long on Tuesday. On Wednesday, Thursday, and Friday he studies for 3 hours each day. He wants to study for a total of 25 hours over the week and divides the remaining amount of study time evenly between Saturday and Sunday. How many hours does Tristan spend studying on Saturday?"""
    # Calculate the total study time from Monday to Friday
    total_weekday_time = 4 + 2 * 4 + 3 * 3

    # Calculate the remaining study time for the weekend
    remaining_time = 25 - total_weekday_time

    # Divide the remaining study time evenly between Saturday and Sunday
    saturday_time = remaining_time / 2

    # Return the result for Saturday study time
    result = saturday_time
    return result

print(solution())