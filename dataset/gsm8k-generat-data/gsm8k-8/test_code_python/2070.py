def solution():
    # Define the number of packs and the percentage that were expired
    total_packs = 80
    expired_percent = 40

    # Calculate the number of expired packs and the number to be returned
    expired_packs = (expired_percent / 100) * total_packs
    returned_packs = expired_packs

    # Calculate the refund amount
    refund_amount = returned_packs * 12
    result = refund_amount
    return result

print(solution())