def solution():
    """Elaina is holding the final concert in her tour. To celebrate her final concert, she makes the concert twice as long as her usual concerts. At the end of the concert, she also performs a 15-minute encore. If the runtime of this final concert is 65 minutes then how long, in minutes, do her usual concerts run for?"""
    final_concert_runtime = 65
    encore_runtime = 15
    usual_concert_runtime = (final_concert_runtime - encore_runtime) / 2
    result = usual_concert_runtime
    return result

print(solution())