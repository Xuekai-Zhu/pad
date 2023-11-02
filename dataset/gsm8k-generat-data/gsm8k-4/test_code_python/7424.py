def solution():
    """ In the honey shop, the bulk price of honey is $5 per pound and the minimum spend is $40 before tax. The honey is taxed at $1 per pound. If Penny has paid $240 for honey, by how many pounds has Penny’s purchase exceed the minimum spend? """
    #Define the bulk price of honey and minimum spend before tax
    bulk_price = 5
    minimum_spend = 40

    #Calculating the amount spent on honey without the tax
    honey_cost_before_tax = 240 - (240 * 0.2)
    
    #Calculating the amount spent on honey after the minimum spend has been met
    honey_cost_after_min_spend = honey_cost_before_tax - minimum_spend
    
    #Calculating the number of pounds of honey purchased above the minimum spend
    honey_purchased = honey_cost_after_min_spend // 6
    
    result = honey_purchased
    return result

print(solution())