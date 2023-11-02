def solution():
    """Billy wants to watch something fun on YouTube but doesn't know what to watch.  He has the website generate 15 suggestions but, after watching each in one, he doesn't like any of them.  Billy's very picky so he does this a total of 5 times before he finally finds a video he thinks is worth watching.  He then picks the 5th show suggested on the final suggestion list.  What number of videos does Billy watch?"""
    # Calculate the total number of videos watched by Billy
    videos_watched = (15 * 5) + 1

    # Display the number of videos watched by Billy
    result = videos_watched
    return result

print(solution())