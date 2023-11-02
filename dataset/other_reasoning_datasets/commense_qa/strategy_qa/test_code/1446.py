def solution():
    statue_of_liberty_height = 305
    statue_of_unity_height = 597
    lighthouse_of_alexandria_height = 363
    # Check if the Statue of Unity is at a similar height as the Statue of Liberty
    if abs(statue_of_liberty_height - statue_of_unity_height) < abs(statue_of_liberty_height - lighthouse_of_alexandria_height):
        result = "yes"
    else:
        result = "no"
    return result

print(solution())