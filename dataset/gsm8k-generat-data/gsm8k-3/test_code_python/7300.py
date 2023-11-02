def solution():
    """John's neighbor tells him to walk his dog for 1 hour each day for a total of $10. He does this for April, save for the 4 Sundays in April. He later spent $50 on books and gave his sister Kaylee the same amount. How much money did John have left?"""
    # Calculate the total amount of money earned walking the dog in April
    total_dog_money = 10 * (30 - 4) # April has 30 days, but John didn't walk the dog on 4 Sundays

    # Calculate the total amount of money spent on books and Kaylee
    total_spending = 50 * 2 # John spent $50 on books and gave Kaylee the same amount

    # Calculate the remaining money John had
    remaining_money = total_dog_money - total_spending

    # Display the remaining money John had
    result = remaining_money
    return result

print(solution())