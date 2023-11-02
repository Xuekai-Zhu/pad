def solution():
    """Mr. Grey is purchasing gifts for his family. So far he has purchased 3 polo shirts for $26 each; 2 necklaces for $83 each; and 1 computer game for $90. Since Mr. Grey purchased all those using his credit card, he received a $12 rebate. What is the total cost of the gifts after the rebate?"""
    polo_shirt_cost = 26
    necklace_cost = 83
    computer_game_cost = 90
    polo_shirt_total = 3 * polo_shirt_cost
    necklace_total = 2 * necklace_cost
    subtotal = polo_shirt_total + necklace_total + computer_game_cost
    total_cost = subtotal - 12
    result = total_cost
    return result

print(solution())