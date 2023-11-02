def solution():
    cost_per_hundred_channels = 100
    total_channels = 200
    channels_per_person = total_channels / 2
    cost_per_person = cost_per_hundred_channels + (cost_per_hundred_channels / 2)
    result = cost_per_person
    return result

print(solution())