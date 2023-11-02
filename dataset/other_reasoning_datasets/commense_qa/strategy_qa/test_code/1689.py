def solution():
    agatha_christie_genre = "mystery"
    jk_rowling_genre = "wizard fantasy"
    robert_galbraith_genre = "mystery"
    if jk_rowling_genre == agatha_christie_genre or jk_rowling_genre == robert_galbraith_genre:
        result = "yes"
    else:
        result = "no"
    return result

print(solution())