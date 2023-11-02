def solution():
    """A reporter is paid by the word and per article. She earns $.1 per word. She earns $60 per article. She has to finish three stories in the next 4 hours. She averages 10 words a minute. How much can she expect to earn per hour if she writes the entire time?"""
    words_per_minute = 10
    words_per_story = 500  # assuming an average article length of 500 words
    pay_per_word = 0.1
    pay_per_article = 60
    total_words = words_per_story * 3
    total_time = 240  # 4 hours in minutes
    writing_time = total_time - (3 * 5)  # subtracting 5 minutes per story for editing and breaks
    total_pay = (total_words * pay_per_word) + (3 * pay_per_article)
    pay_per_hour = total_pay / (writing_time / 60)
    result = pay_per_hour
    return result

print(solution())