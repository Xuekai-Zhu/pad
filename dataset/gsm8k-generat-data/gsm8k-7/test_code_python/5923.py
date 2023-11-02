def solution():
    initial_fireflies = 3
    more_fireflies = 4 + 12
    leaving_fireflies = 2

    # Calculate the total number of fireflies after the new ones arrived
    total_fireflies = initial_fireflies + more_fireflies

    # Calculate the total number of fireflies remaining after some flew away
    remaining_fireflies = total_fireflies - leaving_fireflies
    result = remaining_fireflies
    return result

print(solution())