def solution():
    total_students = 200  # 200 students attended school
    lipstick_wearers = total_students / 2  # Half the students wore lipstick
    red_lipstick_wearers = lipstick_wearers / 4  # One quarter of lipstick wearers wore red lipstick
    blue_lipstick_wearers = red_lipstick_wearers / 5  # One-fifth as many students wore blue lipstick as were wearing red lipstick
    result = blue_lipstick_wearers
    return result

print(solution())