def solution():
    accounting_time = 7  # Maryann spends 7 times as long doing accounting as calling clients
    total_time = 560  # Maryann worked a total of 560 minutes today

    # Calculate the total time spent calling clients and doing accounting
    total_accounting_time = accounting_time / (1 + accounting_time)
    total_calling_time = 1 - total_accounting_time

    # Calculate the time Maryann spent calling clients
    calling_time = total_calling_time * total_time
    result = calling_time
    return result

print(solution())