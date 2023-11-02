def solution():
    """Billy wants to watch something fun on YouTube but doesn't know what to watch. He has the website generate 15 suggestions but, after watching each in one, he doesn't like any of them. Billy's very picky so he does this a total of 5 times before he finally finds a video he thinks is worth watching. He then picks the 5th show suggested on the final suggestion list. What number of videos does Billy watch?"""
    suggestions_per_round = 15
    rounds_until_satisfied = 5
    total_suggestions_watched = suggestions_per_round * rounds_until_satisfied
    final_suggestion_list = list(range(1, suggestions_per_round + 1))
    final_video_choice = final_suggestion_list[4]
    result = total_suggestions_watched
    
    return result

print(solution())