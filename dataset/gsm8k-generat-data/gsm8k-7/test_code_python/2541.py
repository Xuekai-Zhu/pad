def solution():
    bald_eagle_speed = 100  # in miles per hour
    peregrine_falcon_speed = bald_eagle_speed * 2

    bald_eagle_time = 30  # in seconds

    # Calculate the distance that the bald eagle dived
    bald_eagle_distance = bald_eagle_speed * (bald_eagle_time / 3600)

    # Calculate the time it would take the peregrine falcon to dive the same distance
    peregrine_falcon_time = (bald_eagle_distance / peregrine_falcon_speed) * 3600

    result = peregrine_falcon_time
    return result

print(solution())