def solution():
    
    bert_sold = 8
    bert_price = 18
    tory_sold = 7
    tory_price = 20
    bert_earnings = bert_sold * bert_price
    tory_earnings = tory_sold * tory_price
    difference = bert_earnings - tory_earnings
    result = difference
    return result

print(solution())