def solution():
    months_remaining = 3
    listens_so_far = 60000
    listens_per_month = listens_so_far / months_remaining
    total_listens = listens_per_month * months_remaining
    result = total_listens
    return result

print(solution())