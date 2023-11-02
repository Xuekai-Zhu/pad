def solution():
    packs_ordered = 80  # Bob ordered 80 packs of Greek yogurt
    expired_percent = 40  # 40% of the packs were expired
    packs_expired = int(packs_ordered * (expired_percent / 100))  # Calculate the number of expired packs
    packs_returned = packs_expired  # Bob decided to return all the expired packs
    pack_cost = 12  # Each pack costs $12

    # Calculate the refund amount for the expired product
    refund_amount = packs_returned * pack_cost
    result = refund_amount
    return result

print(solution())