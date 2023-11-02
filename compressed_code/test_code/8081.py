def solution():
    
    chlorine_price = 10
    chlorine_discount = 0.2
    soap_price = 16
    soap_discount = 0.25
    num_chlorine = 3
    num_soap = 5
    
    chlorine_discounted_price = chlorine_price * (1 - chlorine_discount)
    chlorine_total_price = chlorine_discounted_price * num_chlorine
    
    soap_discounted_price = soap_price * (1 - soap_discount)
    soap_total_price = soap_discounted_price * num_soap
    
    total_savings = (chlorine_price - chlorine_discounted_price) * num_chlorine + (soap_price - soap_discounted_price) * num_soap
    
    result = total_savings
    return result

print(solution())