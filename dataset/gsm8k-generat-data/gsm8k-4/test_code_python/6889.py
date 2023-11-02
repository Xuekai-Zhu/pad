def solution():
    """Ben has $2000 for his business operations costs. He orders goods from his supplier and writes them a cheque for $600. His debtor pays him $800 from the purchases they had made on credit. Mr. Ben then decides to do equipment maintenance and spends $1200 on the whole operation. How much money is Mr. Ben remaining with?"""
    # Define the initial amount of money
    initial_money = 2000

    # Subtract the cost of ordering goods from the supplier
    initial_money -= 600

    # Add the payment received from the debtor
    initial_money += 800

    # Subtract the cost of equipment maintenance
    initial_money -= 1200

    # Return the remaining amount of money
    result = initial_money
    return result

print(solution())