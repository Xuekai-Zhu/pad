def solution():
    """Osborn is testing a new way to get dressed in the morning on school days so he goes faster and can get up later. He tracks his time for the week and on Monday is takes him 2 minutes. On Tuesday it takes him 4 minutes. On Wednesday it takes him 3 minutes. On Thursday it takes him 4 minutes. Before Friday arrives he looks at his old way of getting dressed and sees that it was taking him 3 minutes on average to get dressed. How fast does he have to get dressed on Friday so his weekly average ties his old method?"""
    old_average = 3
    total_time = 17
    days = 4
    new_average = total_time / 5
    remaining_time = old_average * 5 - total_time
    friday_time = remaining_time if remaining_time > 0 else 0
    result = friday_time
    return result

print(solution())