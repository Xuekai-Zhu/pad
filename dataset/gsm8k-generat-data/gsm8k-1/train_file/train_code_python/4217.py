def solution():
    """Kirill is 14 less centimeters in height than his brother. Together their heights equal 112 centimeters. How tall is Kirill in centimeters?"""
    brother_height = (112 + 14) / 2
    kirill_height = brother_height - 14
    result = kirill_height
    return result

print(solution())