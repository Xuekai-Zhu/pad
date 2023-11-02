def solution():
    # Define the length of rope bought last week and this week
    last_week_rope = 6
    this_week_rope = last_week_rope - 4

    # Convert the length of rope into inches
    total_rope = (last_week_rope + this_week_rope) * 12

    result = total_rope
    return result

print(solution())