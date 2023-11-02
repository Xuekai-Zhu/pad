def solution():
    # Calculate the total number of words the reporter can write in 4 hours
    total_words = 10*60*4  # the reporter averages 10 words a minute and writes for 4 hours

    # Calculate the total amount the reporter can earn from the three articles
    article_pay = 60*3  # the reporter earns $60 per article and has to finish three stories

    # Calculate the total amount the reporter can earn from the words written
    word_pay = 0.1*total_words  # the reporter earns $.1 per word

    # Calculate the total amount the reporter can earn in 4 hours
    total_pay = article_pay + word_pay

    # Calculate the hourly rate for the reporter
    hourly_rate = total_pay/4

    result = hourly_rate
    return result

print(solution())