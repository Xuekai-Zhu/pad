def solution():
    """Gondor is a technician, he earns $10 from repairing a phone and $20 from repairing a laptop. If he was able to repair 3 phones last Monday, 5 phones last Tuesday, 2 laptops on Wednesday, and 4 laptops last Thursday, how much does he earn in total?"""
    phone_repair_fee = 10
    laptop_repair_fee = 20
    phones_repaired = 3 + 5
    laptops_repaired = 2 + 4
    total_fee = (phones_repaired * phone_repair_fee) + (laptops_repaired * laptop_repair_fee)
    result = total_fee
    return result

print(solution())