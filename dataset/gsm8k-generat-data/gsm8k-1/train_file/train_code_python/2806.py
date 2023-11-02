def solution():
    """Osborn is testing a new way to get dressed in the morning on school days so he goes faster and can get up later. He tracks his time for the week and on Monday is takes him 2 minutes. On Tuesday it takes him 4 minutes. On Wednesday it takes him 3 minutes. On Thursday it takes him 4 minutes. Before Friday arrives he looks at his old way of getting dressed and sees that it was taking him 3 minutes on average to get dressed. How fast does he have to get dressed on Friday so his weekly average ties his old method?"""
    old_average = 3
    monday_time = 2
    tuesday_time = 4
    wednesday_time = 3
    thursday_time = 4
    total_time = monday_time + tuesday_time + wednesday_time + thursday_time
    friday_time = (old_average * 5) - total_time
    result = friday_time
    return result

print(solution())