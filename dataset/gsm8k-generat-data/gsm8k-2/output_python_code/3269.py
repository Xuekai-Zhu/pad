def solution():
    """Granger went to the grocery store. He saw that the Spam is $3 per can, the peanut butter is $5 per jar, and the bread is $2 per loaf. If he bought 12 cans of spam, 3 jars of peanut butter, and 4 loaves of bread, how much is the total amount he paid?"""
    spam_price = 3
    peanut_butter_price = 5
    bread_price = 2
    num_cans_of_spam = 12
    num_jars_of_peanut_butter = 3
    num_loaves_of_bread = 4
    total_spam_price = num_cans_of_spam * spam_price
    total_peanut_butter_price = num_jars_of_peanut_butter * peanut_butter_price
    total_bread_price = num_loaves_of_bread * bread_price
    total_price = total_spam_price + total_peanut_butter_price + total_bread_price
    result = total_price
    return result

print(solution())