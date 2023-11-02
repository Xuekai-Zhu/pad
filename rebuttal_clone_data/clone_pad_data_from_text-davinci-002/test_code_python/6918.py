def solution():
     grocery_shopping_texts = 5
     non_responsive_texts = grocery_shopping_texts * 5
     previous_texts = grocery_shopping_texts + non_responsive_texts
     police_texts = previous_texts * 0.1
     total_texts = previous_texts + police_texts
     result = total_texts
     return result

print(solution())