def solution():
    """Jenny's property tax rate is 2%. Her house is currently worth $400,000. The city is about to build a new high-speed rail project nearby, which will increase her house's value by 25%. Jenny can only afford to spend $15,000/year on property tax. How many dollars worth of improvements can she make to her house before her property tax bill gets too high?"""
    current_value = 400000
    valuation_increase = current_value * 0.25
    new_value = current_value + valuation_increase
    property_tax_rate = 0.02
    max_property_tax = 15000
    max_value = (max_property_tax / property_tax_rate) + current_value
    max_improvement = max_value - new_value
    result = max_improvement
    return result

print(solution())