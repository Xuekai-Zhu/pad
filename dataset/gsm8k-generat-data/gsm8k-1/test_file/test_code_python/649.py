def solution():
    """Sally has realized she did not receive a full wage this week. Her bank account, which held $200 at the start of the week, 
    now holds $420. She has received no other money into her bank account this week. If her weekly wage should be $300, how many 
    dollars were withheld from Sally’s wage?"""
    starting_amount = 200
    ending_amount = 420
    weekly_wage = 300
    withheld_amount = weekly_wage - (ending_amount - starting_amount)
    result = withheld_amount
    return result

print(solution())