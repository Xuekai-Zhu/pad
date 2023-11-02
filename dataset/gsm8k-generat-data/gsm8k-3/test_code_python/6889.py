def solution():
    """Ben has $2000 for his business operations costs. He orders goods from his supplier and writes them a cheque for $600. His debtor pays him $800 from the purchases they had made on credit. Mr. Ben then decides to do equipment maintenance and spends $1200 on the whole operation. How much money is Mr. Ben remaining with?"""
    # Initialize with the initial amount Ben had
    remaining_amount = 2000

    # Subtract the cost of goods purchased
    remaining_amount -= 600

    # Add the amount received from the debtor
    remaining_amount += 800

    # Subtract the cost of equipment maintenance
    remaining_amount -= 1200

    # Display the remaining amount
    result = remaining_amount
    return result

print(solution())