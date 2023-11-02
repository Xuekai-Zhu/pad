def solution():
    
    total_students = 50
    bake_likes = 10
    basketball_likes = 5
    music_likes = (total_students - bake_likes - basketball_likes) / 2
    video_likes = music_likes - music_likes
    result = video_likes
    return result

print(solution())