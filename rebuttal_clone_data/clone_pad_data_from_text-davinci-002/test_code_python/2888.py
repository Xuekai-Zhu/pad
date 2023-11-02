def solution():
    chlorine_cost = 10
    chlorine_discount = 20
    soap_cost = 16
    soap_discount = 25
    liters_of_chlorine = 3
    boxes_of_soap = 5
    total_chlorine_cost = chlorine_cost * liters_of_chlorine * (1 - (chlorine_discount / 100))
    total_soap_cost = soap_cost * boxes_of_soap * (1 - (soap_discount / 100))
    total_savings = total_chlorine_cost + total_soap_cost
    result = total_savings
    return result

print(solution())