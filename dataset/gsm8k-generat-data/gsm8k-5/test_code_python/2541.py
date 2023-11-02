def solution():
    bald_eagle_speed = 100  # Bald eagle's diving speed is 100 mph
    peregrine_falcon_speed = bald_eagle_speed * 2  # Peregrine falcon's diving speed is twice that of bald eagle (200 mph)
    bald_eagle_time = 30  # Bald eagle takes 30 seconds to dive to the ground

    # Calculate the time it takes for peregrine falcon to dive the same distance
    peregrine_falcon_time = bald_eagle_time * (bald_eagle_speed / peregrine_falcon_speed)
    result = peregrine_falcon_time
    return result

print(solution())