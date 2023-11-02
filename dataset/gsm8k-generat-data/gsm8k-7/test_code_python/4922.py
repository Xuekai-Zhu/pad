def solution():
    house_price = 500000
    markup_percent = 20
    num_brothers = 3
    tax_percent = 10

    # Calculate the total revenue from selling the house with the markup
    total_revenue = house_price * (1 + markup_percent/100)

    # Calculate the total amount each person gets before taxes
    amount_per_person_before_tax = total_revenue / (num_brothers + 1)

    # Calculate the amount each person gets after taxes
    amount_per_person_after_tax = amount_per_person_before_tax * (1 - tax_percent/100)

    result = amount_per_person_after_tax
    return result

print(solution())