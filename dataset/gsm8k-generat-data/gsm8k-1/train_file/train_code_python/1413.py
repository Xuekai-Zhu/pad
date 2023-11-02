def solution():
    """ Stacy just bought a 6 month prescription of flea & tick medicine for her dog for $150.00 online. Her cashback app was offering 10% cashback and she has a mail-in rebate for $25.00 on a 6-month prescription. How much will the medicine cost after cash back and rebate offers? """
    initial_cost = 150
    cashback_percent = 10
    mail_in_rebate = 25
    
    cashback_amount = initial_cost * (cashback_percent / 100)
    final_cost = initial_cost - mail_in_rebate - cashback_amount
    
    return final_cost

print(solution())