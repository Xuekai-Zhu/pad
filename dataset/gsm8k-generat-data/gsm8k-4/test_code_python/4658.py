def solution():
    """Toby’s father gave him $343 for passing the test. Toby decided to share it with his two brothers, so he gave each of them 1/7 of $343. How many dollars are left for Toby?"""
    # Define the total amount of money Toby's father gave him
    total_money = 343

    # Define the fraction of money that Toby gave to each brother
    fraction = 1/7

    # Calculate the amount of money given to each brother
    brother_money = total_money * fraction

    # Calculate the total amount of money given to both brothers
    total_brother_money = brother_money * 2

    # Calculate the amount of money left for Toby
    toby_money = total_money - total_brother_money

    result = toby_money
    return result

print(solution())