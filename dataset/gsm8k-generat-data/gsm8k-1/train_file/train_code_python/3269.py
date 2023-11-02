def solution():
    """Granger went to the grocery store. He saw that the Spam is $3 per can, the peanut butter is $5 per jar, and the bread is $2 per loaf. If he bought 12 cans of spam, 3 jars of peanut butter, and 4 loaves of bread, how much is the total amount he paid?"""
    spam_price = 3
    peanut_butter_price = 5
    bread_price = 2
    num_spam = 12
    num_peanut_butter = 3
    num_bread = 4
    total_cost = (spam_price * num_spam) + (peanut_butter_price * num_peanut_butter) + (bread_price * num_bread)
    result = total_cost
    return result

print(solution())