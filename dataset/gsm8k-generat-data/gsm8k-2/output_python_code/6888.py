def solution():
    """Ben has $2000 for his business operations costs. He orders goods from his supplier and writes them a cheque for $600. His debtor pays him $800 from the purchases they had made on credit. Mr. Ben then decides to do equipment maintenance and spends $1200 on the whole operation. How much money is Mr. Ben remaining with?"""
    starting_money = 2000
    goods_cost = 600
    debtor_payment = 800
    maintenance_cost = 1200
    remaining_money = starting_money - goods_cost + debtor_payment - maintenance_cost
    result = remaining_money
    return result

print(solution())