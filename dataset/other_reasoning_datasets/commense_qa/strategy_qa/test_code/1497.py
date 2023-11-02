def solution():
    # Define the distance between Israel and Estonia
    distance_israel_estonia = 2000
    # Check if the distance between Israel and Estonia is significant enough that Jesus likely didn't know anyone who spoke Estonian
    if distance_israel_estonia > 100:
        result = "highly unlikely"
    else:
        result = "possible"
    return result

print(solution())