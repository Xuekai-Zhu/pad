def solution():
    gary_gold_grams = 30
    gary_gold_cost = 15

    anna_gold_grams = 50
    anna_gold_cost = 20

    # Calculate the total cost of Gary's gold
    gary_total_cost = gary_gold_grams * gary_gold_cost

    # Calculate the total cost of Anna's gold
    anna_total_cost = anna_gold_grams * anna_gold_cost

    # Calculate the combined cost of their gold
    combined_cost = gary_total_cost + anna_total_cost
    result = combined_cost
    return result

print(solution())