def solution():
    """John brings his dog to the vet. His dog needs 2 vaccines, which are $20 each, and a heartworm check. The heartworm check is 60% of his total bill. If he brought $125 with him, how much does he leave with?"""
    num_vaccines = 2
    vaccine_cost = 20
    subtotal = num_vaccines * vaccine_cost
    heartworm_check = subtotal * 0.6
    total_cost = subtotal + heartworm_check
    amount_paid = 125
    amount_left = amount_paid - total_cost
    result = amount_left
    return result

print(solution())