def solution():
    has_latitude_longitude = True
    can_pinpoint_location = True
    if has_latitude_longitude and can_pinpoint_location:
        result = "yes"
    else:
        result = "no"
    return result

print(solution())