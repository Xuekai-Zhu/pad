def solution():
    property_tax_rate = 2
    house_value = 400000
    high_speed_rail_increase = 25
    max_property_tax_bill = 15000
    increase_in_house_value = house_value * (high_speed_rail_increase / 100)
    new_house_value = increase_in_house_value + house_value
    new_property_tax_bill = new_house_value * (property_tax_rate / 100)
    max_improvement_amount = new_property_tax_bill - max_property_tax_bill
    result = max_improvement_amount
    
    return result

print(solution())