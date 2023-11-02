def solution():
    original_jellybeans = 90
    Samantha_jellybeans = 24
    Shelby_jellybeans = 12
    jellybeans_taken = Samantha_jellybeans + Shelby_jellybeans
    jellybeans_refilled = jellybeans_taken / 2
    jellybeans_now = original_jellybeans - jellybeans_taken + jellybeans_refilled
    result = jellybeans_now
    return result

print(solution())