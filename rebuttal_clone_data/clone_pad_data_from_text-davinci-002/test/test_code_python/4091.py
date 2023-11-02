def solution():
    total_photos_needed = 40
    photos_brought_by_cristina = 7
    photos_brought_by_john = 10
    photos_brought_by_sarah = 9
    photos_brought_by_clarissa = total_photos_needed - photos_brought_by_cristina - photos_brought_by_john - photos_brought_by_sarah
    result = photos_brought_by_clarissa
    return result

print(solution())