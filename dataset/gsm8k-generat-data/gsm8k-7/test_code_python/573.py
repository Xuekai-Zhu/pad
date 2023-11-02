def solution():
    num_bert_phones = 8
    bert_phone_price = 18

    num_tory_guns = 7
    tory_gun_price = 20

    # Calculate the total earnings of Bert and Tory
    bert_earnings = num_bert_phones * bert_phone_price
    tory_earnings = num_tory_guns * tory_gun_price

    # Calculate the difference in earnings between Bert and Tory
    diff_earnings = bert_earnings - tory_earnings
    result = diff_earnings
    return result

print(solution())