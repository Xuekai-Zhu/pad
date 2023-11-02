def solution():
    temperature_range = [-10.5, 1.4]
    comfortable_temperature_range = [15, 30]
    if any([temp<comfortable_temperature_range[0] or temp>comfortable_temperature_range[1] for temp in temperature_range]):
        result = "no"
    else:
        result = "yes"
    return result

print(solution())