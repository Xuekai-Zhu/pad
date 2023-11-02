def solution():
    spam_price = 3
    num_cans_spam = 12

    peanut_butter_price = 5
    num_jars_peanut_butter = 3

    bread_price = 2
    num_loaves_bread = 4

    # Calculate the total cost of all cans of spam
    total_spam_cost = spam_price * num_cans_spam

    # Calculate the total cost of all jars of peanut butter
    total_peanut_butter_cost = peanut_butter_price * num_jars_peanut_butter

    # Calculate the total cost of all loaves of bread
    total_bread_cost = bread_price * num_loaves_bread

    # Calculate the total amount Granger paid
    total_amount_paid = total_spam_cost + total_peanut_butter_cost + total_bread_cost
    result = total_amount_paid
    return result

print(solution())