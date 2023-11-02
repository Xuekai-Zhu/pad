def solution():
    fritz_money = 40

    # Calculate Sean's money
    sean_money = (fritz_money / 2) + 4

    # Calculate Rick's money
    rick_money = sean_money * 3

    # Calculate total money of Rick and Sean
    total_money = sean_money + rick_money
    result = total_money
    return result

print(solution())