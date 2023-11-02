def solution():
    suggestions_per_round = 15  # Billy gets 15 video suggestions per round
    rounds_before_finding_video = 5  # Billy goes through 5 rounds of suggestions before finding a video he likes
    videos_watched_before_finding_video = suggestions_per_round * rounds_before_finding_video  # Billy watches this many videos before finding one he likes
    video_picked_on_final_suggestion_list = 5  # Billy picks the 5th video on the final suggestion list

    # Calculate the total number of videos Billy watches
    total_videos_watched = videos_watched_before_finding_video + video_picked_on_final_suggestion_list
    result = total_videos_watched
    return result

print(solution())