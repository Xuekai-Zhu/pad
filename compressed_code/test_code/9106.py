def solution():
    
    budget = 500
    maths_books = 4
    science_books = maths_books + 6
    art_books = maths_books * 2
    maths_cost = maths_books * 20
    science_cost = science_books * 10
    art_cost = art_books * 20
    total_spent = maths_cost + science_cost + art_cost
    music_cost = budget - total_spent
    result = music_cost
    
    return result

print(solution())