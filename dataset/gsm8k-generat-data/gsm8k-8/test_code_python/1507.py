def solution():
    # Define Fritz's amount of money
    fritz_money = 40

    # Calculate Sean's amount of money
    sean_money = 0.5 * fritz_money + 4

    # Calculate Rick's amount of money
    rick_money = 3 * sean_money

    # Calculate the total amount of money Sean and Rick have
    sean_and_rick_money = sean_money + rick_money
    result = sean_and_rick_money
    return result

print(solution())