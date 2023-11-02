def solution():
    fresh_parsley_storage = "cool"
    dry_parsley_storage = "shelf stable"
    if fresh_parsley_storage != dry_parsley_storage:
        result = "yes"
    else:
        result = "no"
    return result

print(solution())