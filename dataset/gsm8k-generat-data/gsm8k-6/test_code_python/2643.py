def solution():
    # Calculate the total minutes Brian spends watching animal videos
    cat_video = 4  # minutes
    dog_video = 2 * cat_video  # minutes
    gorilla_video = 2 * (cat_video + dog_video)  # minutes
    total_minutes = cat_video + dog_video + gorilla_video
    result = total_minutes
    return result

print(solution())