def solution():
    words_per_minute = 10
    pay_per_word = 0.1
    pay_per_article = 60
    articles_to_write = 3
    writing_time_in_hours = 4
    time_to_write_one_article_in_minutes = writing_time_in_hours * 60 / articles_to_write
    words_to_write = time_to_write_one_article_in_minutes * words_per_minute
    total_pay = words_to_write * pay_per_word + pay_per_article * articles_to_write
    pay_per_hour = total_pay / writing_time_in_hours
    result = pay_per_hour
    
    return result

print(solution())