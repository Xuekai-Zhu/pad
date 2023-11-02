def solution():
    """John's neighbor tells him to walk his dog for 1 hour each day for a total of $10. He does this for April, save for the 4 Sundays in April. He later spent $50 on books and gave his sister Kaylee the same amount. How much money did John have left?"""
    # Calculate the total amount earned by walking the dog
    earnings = 10 * (30 - 4)

    # Calculate the total amount spent on books and given to Kaylee
    expenses = 50 * 2

    # Calculate the final amount of money John has left
    final_amount = earnings - expenses

    result = final_amount
    return result

print(solution())