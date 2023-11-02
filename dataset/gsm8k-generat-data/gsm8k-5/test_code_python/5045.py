def solution():
    rope_last_week = 6  # Mr. Sanchez bought 6 feet of rope last week
    rope_this_week = rope_last_week - 4  # Mr. Sanchez bought 4 feet less than last week
    total_rope = rope_last_week + rope_this_week  # Calculate the total amount of rope bought in feet
    inches_per_foot = 12  # There are 12 inches in a foot

    # Calculate the total amount of rope bought in inches
    total_rope_inches = total_rope * inches_per_foot
    result = total_rope_inches
    return result

print(solution())