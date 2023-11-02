def solution():
    
    top_level = 64
    previous_level = top_level / 0.8
    second_level = previous_level / 0.8
    third_level = second_level / 0.8
    total_books = top_level + previous_level + second_level + third_level
    result = total_books
    return result

print(solution())