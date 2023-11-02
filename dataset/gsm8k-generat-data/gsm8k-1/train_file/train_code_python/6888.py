def solution():
    """Ben has $2000 for his business operations costs. He orders goods from his supplier and writes them a cheque for $600. His debtor pays him $800 from the purchases they had made on credit. Mr. Ben then decides to do equipment maintenance and spends $1200 on the whole operation. How much money is Mr. Ben remaining with?"""
    initial_funds = 2000
    order_cost = 600
    debtor_payment = 800
    maintenance_cost = 1200
    total_expenses = order_cost + maintenance_cost
    total_income = debtor_payment
    remaining_funds = initial_funds + total_income - total_expenses
    result = remaining_funds
    return result

print(solution())