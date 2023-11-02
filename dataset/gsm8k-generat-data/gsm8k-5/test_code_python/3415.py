def solution():
    kids_fee = 3  # Jose charges $3 for kids
    adults_fee = 6  # Jose charges twice the amount for adults

    # Calculate the total daily revenue
    daily_revenue = (kids_fee * 8) + (adults_fee * 10)  # 8 kids and 10 adults swim per day

    # Calculate the weekly revenue
    weekly_revenue = daily_revenue * 7  # Jose charges for 7 days a week

    result = weekly_revenue
    return result

print(solution())