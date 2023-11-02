def solution():
    """Jane's mother agreed to pay her $.50 for every flower bulb that Jane planted. Jane planted 20 tulip bulbs and half that amount of iris bulbs. She also planted 30 daffodil bulbs and three times that amount of crocus bulbs. How much money did Jane earn?"""
    tulip_bulbs = 20
    iris_bulbs = tulip_bulbs / 2
    daffodil_bulbs = 30
    crocus_bulbs = 3 * daffodil_bulbs

    total_bulbs = tulip_bulbs + iris_bulbs + daffodil_bulbs + crocus_bulbs
    earning_per_bulb = 0.5
    total_earning = total_bulbs * earning_per_bulb
    result = total_earning
    return result

print(solution())