def solution():
    total_amount = 500
    number_of_maths_books = 4
    cost_of_maths_books = 20
    number_of_science_books = number_of_maths_books + 6
    cost_of_science_books = 10
    number_of_art_books = number_of_maths_books * 2
    cost_of_art_books = 20
    cost_of_music_books = (total_amount - (cost_of_maths_books * number_of_maths_books) - (cost_of_science_books * number_of_science_books) - (cost_of_art_books * number_of_art_books)) / 1
     
    result = cost_of_music_books
    return result

print(solution())