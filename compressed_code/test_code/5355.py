def solution():
    
    grocery_texts = 5
    response_texts = 5 * grocery_texts
    police_texts = 0.1 * (grocery_texts + response_texts)
    total_texts = grocery_texts + response_texts + police_texts
    result = total_texts
    return result

print(solution())