def solution():
    """James paints a 20 ft by 15 ft mural. It takes him 20 minutes to paint 1 square foot and he charges $150 per hour. How much does he charge to paint the mural?"""
    mural_width = 20
    mural_height = 15
    square_feet = mural_width * mural_height
    time_per_square_foot = 20  # in minutes
    time_per_hour = 60  # in minutes
    time_taken = square_feet * time_per_square_foot
    hourly_rate = 150
    amount_charged = (time_taken / time_per_hour) * hourly_rate
    result = amount_charged
    return result

print(solution())