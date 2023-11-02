def solution():
     """Missy had a giant piggy bank in her bedroom. Every day she would search the house for change to put in her bank. After 4 years, the bank was opened and it contained $450 in change. If the second, third, and fourth-year she doubled the amount of money she put in the bank from the amount she had put in the previous year, how much money, in dollars, did she put in the bank the first year?"""
     money_in_bank = 450
     money_year_two = money_in_bank / 2
     money_year_three = money_year_two / 2
     money_year_four = money_year_three / 2
     total_money = money_in_bank + money_year_two + money_year_three + money_year_four
     money_year_one = total_money - money_in_bank - money_year_two - money_year_three - money_year_four
     result = money_year_one
     return result

print(solution())