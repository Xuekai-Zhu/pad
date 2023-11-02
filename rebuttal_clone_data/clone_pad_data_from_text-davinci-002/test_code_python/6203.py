def solution():
    total_spoons = 7
    total_cost = 21
    cost_per_spoon = total_cost / total_spoons
    spoons_to_buy = 5
    total_cost = cost_per_spoon * spoons_to_buy
    result = total_cost
    return result

 Question: A recipe for a smoothie requires 1 cup of milk and 2 bananas.  If I have 2 cups of milk and 5 bananas, how many smoothies can I make?
 Solution: 
def solution():
    milk_needed = 1
    bananas_needed = 2
    total_needed = milk_needed + bananas_needed
    milk_available = 2
    bananas_available = 5
    total_available = milk_available + bananas_available
    items_needed_per_smoothie = milk_needed + bananas_needed
    items_available_per_smoothie = milk_available + bananas_available
    smoothies_possible = total_available // items_needed_per_smoothie
    result = smoothies_possible
    return result

print(solution())