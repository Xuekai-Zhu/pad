def solution():
    tulip_bulbs = 20  # Jane planted 20 tulip bulbs
    iris_bulbs = tulip_bulbs / 2  # Jane planted half the amount of iris bulbs as tulip bulbs
    daffodil_bulbs = 30  # Jane planted 30 daffodil bulbs
    crocus_bulbs = 3 * daffodil_bulbs  # Jane planted three times the amount of crocus bulbs as daffodil bulbs

    total_bulbs = tulip_bulbs + iris_bulbs + daffodil_bulbs + crocus_bulbs  # Calculate the total number of bulbs planted
    earnings = total_bulbs * 0.5  # Jane earns $0.50 for every bulb planted

    result = earnings
    return result

print(solution())