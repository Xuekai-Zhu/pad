def solution():
    
    total_chapters = 31
    read_chapters = total_chapters - (total_chapters // 3)
    time_per_chapter = 20/60  
    total_time = read_chapters * time_per_chapter
    result = total_time
    return result

print(solution())