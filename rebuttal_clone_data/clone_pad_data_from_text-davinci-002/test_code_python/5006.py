def solution():
    packs_of_candy = 3
    bill_paid = 20
    change_received = 11
    cost_per_pack = (bill_paid - change_received) / packs_of_candy
    result = cost_per_pack
    return result

print(solution())