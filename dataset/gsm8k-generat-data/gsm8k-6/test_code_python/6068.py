def solution():
    initial_balance = 25  # initial balance of Tabitha
    mom_amount = 8  # amount given to mom
    remaining_balance = initial_balance - mom_amount  # balance after giving money to mom
    investment_amount = remaining_balance / 2  # amount invested in the money market
    item_cost = 0.5  # cost of each item
    item_quantity = 5  # number of items purchased
    item_total_cost = item_cost * item_quantity  # total cost of the items
    remaining_balance -= item_total_cost  # remaining balance after buying the items
    remaining_balance -= investment_amount  # remaining balance after investing
    result = remaining_balance
    return result

print(solution())