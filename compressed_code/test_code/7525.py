def solution():
    
    members = 6
    snacks_fee = 150
    hardcover_fee = 30
    paperback_fee = 12
    total_fee = (snacks_fee + (hardcover_fee * 6) + (paperback_fee * 6)) * members
    result = total_fee
    return result

print(solution())