def solution():
    """A smartphone seller is offering a discount of 5% off for customers who buy at least 2 smartphones at once. Melinda, Zoe and Joel want to buy an iPhone X each. If an iPhone X costs $600, how much can they save by pooling their money together and buying three iPhones at once from this seller rather than buying individually?"""
    num_phones = 3
    phone_cost = 600
    total_cost = num_phones * phone_cost
    discount_threshold = 2
    discount_percent = 5
    if num_phones >= discount_threshold:
        total_cost *= (100 - discount_percent) / 100
    individual_cost = phone_cost
    individual_total_cost = individual_cost * num_phones
    saved_amount = individual_total_cost - total_cost
    result = saved_amount
    return result

print(solution())