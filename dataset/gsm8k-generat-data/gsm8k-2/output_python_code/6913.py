def solution():
    """Billy wants to watch something fun on YouTube but doesn't know what to watch. He has the website generate 15 suggestions but, after watching each in one, he doesn't like any of them. Billy's very picky so he does this a total of 5 times before he finally finds a video he thinks is worth watching. He then picks the 5th show suggested on the final suggestion list. What number of videos does Billy watch?"""
    suggestions_per_round = 15
    rounds_before_finding_watchable_video = 5
    videos_watched = suggestions_per_round * rounds_before_finding_watchable_video
    videos_watched += 5
    result = videos_watched
    return result

print(solution())