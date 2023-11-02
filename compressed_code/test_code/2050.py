def solution():
    
    school_price = 45
    outside_price = school_price * 0.8
    num_textbooks = 3
    school_total = school_price * num_textbooks
    outside_total = outside_price * num_textbooks
    amount_saved = school_total - outside_total
    result = amount_saved
    return result

print(solution())