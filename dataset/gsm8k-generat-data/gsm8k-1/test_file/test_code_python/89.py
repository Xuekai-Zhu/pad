def solution():
    """Lee used to be able to run the 400-meter hurdles two seconds faster than Gerald would run the 400-meter hurdles.
    But Gerald changed his diet, which improved his speed by 10%. If Lee runs the 400-meter hurdles in 38 seconds,
    how fast can Gerald, with his improved diet, run the 400-meter hurdles, in seconds?"""
    lee_time = 38
    lee_faster_than_gerald = 2
    gerald_improves_by_percent = 10
    gerald_original_time = lee_time + lee_faster_than_gerald
    gerald_improved_time = gerald_original_time - (gerald_original_time * (gerald_improves_by_percent / 100))

    result = gerald_improved_time
    return result

print(solution())