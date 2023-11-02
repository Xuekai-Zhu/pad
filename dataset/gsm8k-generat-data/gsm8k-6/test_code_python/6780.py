def solution():
    # Calculate how long Chuck can ride the merry-go-round
    chuck_time = 5 * 10  # Chuck can ride 5 times longer than Dave who can ride for 10 minutes

    # Calculate how long Erica can ride the merry-go-round
    erica_time = chuck_time * 1.3  # Erica can stay on 30% longer than Chuck
    result = erica_time
    return result

print(solution())