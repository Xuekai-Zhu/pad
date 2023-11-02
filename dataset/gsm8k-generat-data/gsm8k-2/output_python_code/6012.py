def solution():
    """Melisa and Jennifer threw a fiftieth birthday party for their father at a local restaurant. When the bill came, Melisa added a 15% tip of $42. Jennifer said that the service was wonderful and they should leave a 20% tip instead. How much is a 20% tip?"""
    melisa_tip_percentage = 15
    jennifer_tip_percentage = 20
    melisa_tip_amount = 42
    bill_amount = melisa_tip_amount / (melisa_tip_percentage / 100)
    jennifer_tip_amount = bill_amount * (jennifer_tip_percentage / 100)
    result = jennifer_tip_amount
    return result

print(solution())