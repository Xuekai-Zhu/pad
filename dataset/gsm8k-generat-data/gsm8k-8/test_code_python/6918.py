def solution():
    grocery_texts = 5
    non_responding_texts = 5 * grocery_texts
    police_texts = 0.1 * (grocery_texts + non_responding_texts)
    total_texts = grocery_texts + non_responding_texts + police_texts
    result = total_texts
    return result

print(solution())