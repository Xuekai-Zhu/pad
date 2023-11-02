def solution():
    audiobooks = 6  # Fernanda purchased 6 Audiobooks
    audiobook_length = 30  # Each audiobook is 30 hours long
    daily_listening_time = 2  # Fernanda listens to 2 hours of an audiobook each day

    # Calculate the total time it takes Fernanda to finish all the audiobooks
    total_listening_time = audiobooks * audiobook_length
    total_days = total_listening_time / daily_listening_time

    result = total_days
    return result

print(solution())