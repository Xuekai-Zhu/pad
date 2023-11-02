def solution():
    """Bethany can run 10 laps on the track in one hour. Trey can run 4 more laps than Bethany. Shaelyn can run half as many laps as Trey. Quinn can run 2 fewer laps than Shaelyn. How many more laps can Bethany run compared to Quinn?"""
    laps_bethany = 10
    laps_trey = laps_bethany + 4
    laps_shaelyn = laps_trey / 2
    laps_quinn = laps_shaelyn - 2
    difference = laps_bethany - laps_quinn
    result = difference
    return result

print(solution())