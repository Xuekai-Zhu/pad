def solution():
    
    chlorine_price = 10
    chlorine_discount = 0.2
    soap_price = 16
    soap_discount = 0.25
    num_chlorine = 3
    num_soap = 5
    
    total_chlorine_price = chlorine_price * num_chlorine
    total_chlorine_discount = total_chlorine_price * chlorine_discount
    total_soap_price = soap_price * num_soap
    total_soap_discount = total_soap_price * soap_discount
    
    total_savings = total_chlorine_discount + total_soap_discount
    result = total_savings
    return result

print(solution())