def solution():
    chlorine_price = 10
    chlorine_discount = 0.2  # 20% off
    soap_price = 16
    soap_discount = 0.25  # 25% off
    num_chlorine = 3
    num_soap = 5

    # Calculate the discounted price of one liter of chlorine
    discounted_chlorine_price = chlorine_price * (1 - chlorine_discount)

    # Calculate the discounted price of one box of soap
    discounted_soap_price = soap_price * (1 - soap_discount)

    # Calculate the total savings on chlorine
    chlorine_savings = num_chlorine * (chlorine_price - discounted_chlorine_price)

    # Calculate the total savings on soap
    soap_savings = num_soap * (soap_price - discounted_soap_price)

    # Calculate the total savings
    total_savings = chlorine_savings + soap_savings
    result = total_savings
    return result

print(solution())