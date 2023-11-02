def solution():
    tulip_bulbs = 20
    iris_bulbs = tulip_bulbs / 2
    daffodil_bulbs = 30
    crocus_bulbs = daffodil_bulbs * 3

    # Calculate the total number of flower bulbs planted
    total_bulbs = tulip_bulbs + iris_bulbs + daffodil_bulbs + crocus_bulbs

    # Calculate the amount of money earned by multiplying the total number of bulbs by the payment per bulb
    payment_per_bulb = 0.5
    total_earned = total_bulbs * payment_per_bulb
    result = total_earned
    return result

print(solution())