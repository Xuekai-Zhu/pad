def solution():
    cat_video = 4
    dog_video = 2 * cat_video
    gorilla_video = 2 * (cat_video + dog_video)

    total_minutes = cat_video + dog_video + gorilla_video
    result = total_minutes
    return result

print(solution())