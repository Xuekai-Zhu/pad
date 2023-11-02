def solution():
    drums_per_day = 18/3  # The paint mixer makes 6 drums of paint each day
    total_drums = 360  # The paint mixer needs to make 360 drums of paint

    # Calculate the number of days it will take to make 360 drums of paint
    days_required = total_drums / drums_per_day
    result = days_required
    return result

print(solution())