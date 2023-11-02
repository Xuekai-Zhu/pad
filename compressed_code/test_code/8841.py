def solution():
    
    initial_volume = 220
    percent_loss = 10
    volume_remaining = initial_volume - (initial_volume * (percent_loss / 100))
    result = volume_remaining
    return result

print(solution())