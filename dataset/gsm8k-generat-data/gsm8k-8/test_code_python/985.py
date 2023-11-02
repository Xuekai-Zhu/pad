def solution():
    num_of_pages = 42
    num_of_crumpled = num_of_pages // 7
    num_of_blurred = num_of_pages // 3
    num_of_crumpled_and_blurred = num_of_pages // 21
    
    total_faulty_pages = num_of_crumpled + num_of_blurred - num_of_crumpled_and_blurred
    num_of_perfect_pages = num_of_pages - total_faulty_pages
    
    result = num_of_perfect_pages
    return result

print(solution())