def solution():
    # Define the distance from Alcatraz Island to Siberia, and the longest continuous swim record
    distance = 5217
    swim_record = 139
    # Check if the distance is greater than the swim record
    if distance > swim_record:
        result = "no"
    else:
        result = "yes"
    return result

print(solution())