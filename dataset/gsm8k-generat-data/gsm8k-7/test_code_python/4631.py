def solution():
    pay_per_word = 0.1
    pay_per_article = 60
    num_articles = 3
    time_in_minutes = 4 * 60
    words_per_minute = 10

    # Calculate the total number of words the reporter can write in 4 hours
    total_words = time_in_minutes * words_per_minute

    # Calculate the total pay the reporter will earn from writing articles
    total_pay = (pay_per_word * total_words) + (pay_per_article * num_articles)

    # Calculate the hourly pay the reporter can expect to earn if she writes the entire time
    hourly_pay = total_pay / 4
    result = hourly_pay
    return result

print(solution())