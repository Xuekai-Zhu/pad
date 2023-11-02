def solution():
    # Calculate the total number of texts Jennifer's boyfriend sent
    grocery_texts = 5
    follow_up_texts = 5 * 5  # 5 times more texts than the grocery texts
    police_texts = int((grocery_texts + follow_up_texts) * 0.1)  # 10% of all texts sent previously
    total_texts = grocery_texts + follow_up_texts + police_texts
    result = total_texts
    return result

print(solution())