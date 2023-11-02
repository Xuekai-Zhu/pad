def solution():
    # Calculate the speed of the peregrine falcon
    eagle_speed = 100
    falcon_speed = 2 * eagle_speed  # the peregrine falcon can dive at a speed of twice that of the bald eagle

    # Calculate the time it takes for the peregrine falcon to dive the same distance
    eagle_time = 30
    falcon_time = eagle_time * (eagle_speed / falcon_speed)

    result = falcon_time
    return result

print(solution())