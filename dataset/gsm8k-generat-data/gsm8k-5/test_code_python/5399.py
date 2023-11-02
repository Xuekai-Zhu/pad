def solution():
    total_copies = 1000000
    advance_copies = 100000
    sold_copies = total_copies - advance_copies

    steve_profit = sold_copies * 2
    agent_fee = steve_profit * 0.1
    total_profit = steve_profit - agent_fee

    result = total_profit
    return result

print(solution())