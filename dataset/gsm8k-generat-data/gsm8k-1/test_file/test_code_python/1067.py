def solution():
    """Kayla is having her birthday party at a movie theater. The fee to rent the theater is $125 for a party of 20, plus $6 for each additional guest. Kayla invited her 25 classmates and the 7 girls in her dance class, as well as 13 family members. Only 4 people said they could not come. How much will the party cost?"""
    base_fee = 125
    total_guests = 25 + 7 + 13 - 4
    extra_guests = total_guests - 20
    extra_fee = extra_guests * 6
    total_cost = base_fee + extra_fee
    result = total_cost
    return result

print(solution())