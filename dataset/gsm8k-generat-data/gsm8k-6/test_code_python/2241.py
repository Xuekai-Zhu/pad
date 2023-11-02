def solution():
    # Calculate the distance traveled by the coyote in 1 hour
    coyote_distance = 15  # miles per hour

    # Calculate the distance Darrel needs to cover to catch up to the coyote
    distance_to_travel = coyote_distance  # since Darrel starts 1 hour later, he needs to travel the distance of 1 hour of coyote's speed

    # Calculate the time it will take for Darrel to catch up to the coyote
    time_taken = distance_to_travel / (30 - 15)  # relative speed of Darrel's motorbike and the coyote is 30-15=15 miles per hour

    result = time_taken
    return result

print(solution())