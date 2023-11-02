def solution():
    """Lorie has 2 pieces of $100 bills. He requested to change one piece of the $100 bills into $50 bills. Half of the remaining $100 bill is changed to $10 bills while the rest is changed to $5 bills. How many pieces of bills will she have?"""
    # Lorie starts with 2 pieces of $100 bills
    starting_bills = 2
    # She changes one $100 bill into 2 $50 bills, so she now has 3 bills
    after_fifty_bills = starting_bills + 1
    # Half of the remaining $100 bill is changed into $10 bills, so she now has 4 bills
    after_ten_bills = after_fifty_bills + 1
    # The other half of the remaining $100 bill is changed into $5 bills, so she now has 5 bills in total
    after_five_bills = after_ten_bills + 1
    result = after_five_bills
    return result

print(solution())