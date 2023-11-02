def solution():
    
    pineapple_price = 6
    mango_price = 5
    total_spent = 94
    pineapple_spent = 54
    mango_spent = total_spent - pineapple_spent
    pineapple_count = pineapple_spent // pineapple_price
    mango_count = mango_spent // mango_price
    total_people = pineapple_count + mango_count
    result = total_people
    return result

print(solution())