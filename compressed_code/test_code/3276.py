def solution():
    
    budget = 500
    math_books = 4
    science_books = math_books + 6
    art_books = math_books * 2
    math_cost = math_books * 20
    science_cost = science_books * 10
    art_cost = art_books * 20
    total_spent = math_cost + science_cost + art_cost
    music_cost = budget - total_spent
    result = music_cost
    return result

print(solution())