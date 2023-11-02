def solution():
    """A shopkeeper bought 150 packets of milk. Each packet contained 250 ml of milk. If one fluid ounce is equal to 30 ml, how many ounces of milk did he buy?"""
    packets_of_milk = 150
    ml_per_packet = 250
    ml_to_oz_conversion = 30
    total_ml = packets_of_milk * ml_per_packet
    total_oz = total_ml / ml_to_oz_conversion
    result = total_oz
    
    return result

print(solution())