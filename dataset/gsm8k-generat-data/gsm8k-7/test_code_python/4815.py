def solution():
    bracelets = 30
    price_each = 5
    price_two_for_eight = 8
    income_from_fives = 60

    # Calculate the total income from selling bracelets at regular price
    income_from_regular_sales = income_from_fives

    # Calculate how many bracelets were sold at regular price
    num_regular_sales = income_from_regular_sales // price_each

    # Calculate how many bracelets were sold at the discounted price
    num_discounted_sales = bracelets - num_regular_sales

    # Calculate the income from the discounted sales
    income_from_discounted_sales = (num_discounted_sales // 2) * price_two_for_eight

    # Calculate the total income from selling all bracelets
    total_income = income_from_regular_sales + income_from_discounted_sales
    result = total_income
    return result

print(solution())