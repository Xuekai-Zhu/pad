def solution():
    """Steve and Tim decide to see who can get home from school the fastest. Steve lives further away than Tim, so he is allowed to ride his bike. Steve lives 3 miles from the school and can bike at 440 feet per minute. Tim lives 2 miles away from the school. If Tim can ride his skateboard at 264 feet per minute, how long will the winner be waiting at their house before the loser finishes the race?"""
    steve_distance = 3 * 5280  # converting miles to feet
    tim_distance = 2 * 5280  # converting miles to feet
    steve_speed = 440
    tim_speed = 264
    steve_time = steve_distance / steve_speed
    tim_time = tim_distance / tim_speed
    winner_waiting_time = abs(steve_time - tim_time) / 60  # converting to minutes
    result = winner_waiting_time
    return result

print(solution())