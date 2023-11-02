def solution():
     old_number_of_texts = 20
     new_number_of_texts = 55
     texts_intended_for_him = old_number_of_texts
     texts_not_intended_for_him = new_number_of_texts - texts_intended_for_him
     texts_per_week = texts_not_intended_for_him * 7
     result = texts_per_week
     return result

print(solution())