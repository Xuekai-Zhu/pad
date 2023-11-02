def solution():
    """Billy wants to watch something fun on YouTube but doesn't know what to watch. He has the website generate 15 suggestions but, after watching each in one, he doesn't like any of them. Billy's very picky so he does this a total of 5 times before he finally finds a video he thinks is worth watching. He then picks the 5th show suggested on the final suggestion list. What number of videos does Billy watch?"""
    # Define the number of suggestions generated each time
    suggestions_each_time = 15

    # Define the number of times Billy searches for a video
    search_times = 5

    # Calculate the total number of videos Billy watches
    total_watched = suggestions_each_time * search_times

    # Calculate the number of suggestions in the final list
    final_suggestions = suggestions_each_time ** search_times

    # Calculate the index of the video Billy chooses in the final suggestion list
    chosen_index = 5

    # Calculate the number of videos Billy watches before finding the one he likes
    watched_before_chosen = (final_suggestions - chosen_index) * search_times

    # Calculate the total number of videos Billy watches
    total_watched += watched_before_chosen

    result = total_watched
    return result

print(solution())