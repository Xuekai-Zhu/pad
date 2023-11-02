def solution():
    members = 6
    annual_fee = 150
    hardcover_fee = 30
    paperback_fee = 12
    total_fees = (annual_fee * members) + (hardcover_fee * members) + (paperback_fee * members)
    result = total_fees
    return result

print(solution())