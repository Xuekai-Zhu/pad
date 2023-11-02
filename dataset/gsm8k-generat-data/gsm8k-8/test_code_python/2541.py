def solution():
    # Define the speed of the bald eagle and calculate the speed of the peregrine falcon
    bald_eagle_speed = 100
    peregrine_falcon_speed = bald_eagle_speed * 2

    # Define the time it takes the bald eagle to dive and use it to calculate the distance
    bald_eagle_time = 30
    bald_eagle_distance = bald_eagle_speed * bald_eagle_time

    # Calculate the time it would take the peregrine falcon to dive the same distance
    peregrine_falcon_time = bald_eagle_distance / peregrine_falcon_speed
    result = peregrine_falcon_time
    return result

print(solution())