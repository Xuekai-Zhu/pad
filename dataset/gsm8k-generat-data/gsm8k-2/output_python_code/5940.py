def solution():
    """Aunt May milks her cows twice a day. This morning she got 365 gallons of milk. This evening she got 380 gallons. She sold 612 gallons to the local ice cream factory. She had 15 gallons left over from yesterday. How many gallons of milk does she have left?"""
    total_milk = (365 + 380) * 2 + 15
    sold_milk = 612
    remaining_milk = total_milk - sold_milk
    result = remaining_milk
    return result

print(solution())