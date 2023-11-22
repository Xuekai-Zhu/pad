def solution():
    
    total_students = 50
    bake_hobbies = 10
    basketball_hobbies = 5
    music_hobbies = (total_students - bake_hobbies - basketball_hobbies) / 3
    games_hobbies = total_students - bake_hobbies - basketball_hobbies
    games_playing = games_hobbies * 2
    result = games_playing
    return result

print(solution())