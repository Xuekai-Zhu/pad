def solution():
    accounting_time = 7
    total_time = 560
    calling_clients_time = total_time / (accounting_time + 1)
    result = calling_clients_time
    return result

print(solution())