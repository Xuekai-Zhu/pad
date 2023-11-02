def solution():
    """James paints a 20 ft by 15 ft mural. It takes him 20 minutes to paint 1 square foot and he charges $150 per hour. How much does he charge to paint the mural?"""
    mural_size = 20 * 15  # in square feet
    paint_time = mural_size * 20  # in minutes
    paint_time_hours = paint_time / 60
    hourly_rate = 150
    total_charge = paint_time_hours * hourly_rate
    result = total_charge
    return result

print(solution())