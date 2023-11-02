def solution():
    cans_of_spam = 12
    price_per_can_of_spam = 3
    jars_of_peanut_butter = 3
    price_per_jar_of_peanut_butter = 5
    loaves_of_bread = 4
    price_per_loaf_of_bread = 2

    # Calculate the total cost of the Spam
    total_cost_of_spam = cans_of_spam * price_per_can_of_spam

    # Calculate the total cost of the peanut butter
    total_cost_of_peanut_butter = jars_of_peanut_butter * price_per_jar_of_peanut_butter

    # Calculate the total cost of the bread
    total_cost_of_bread = loaves_of_bread * price_per_loaf_of_bread

    # Calculate the total amount paid by Granger
    total_amount_paid = total_cost_of_spam + total_cost_of_peanut_butter + total_cost_of_bread
    result = total_amount_paid
    return result

print(solution())