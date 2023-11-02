Unfortunately, as an AI language model, I am unable to provide a solution for the question about Samantha's last name as it requires further information about Bobbie's last name and Jamie's last name. Can you please provide more details or rephrase the question?

Regarding the second question, here's a possible solution:

def solution():
    """Peter has $70 and wishes to spend an equal amount each day for one week. From Sunday through Wednesday, he spent his money on wooden action figures which cost $5 each. For the rest of the week, he will buy plastic action figures which cost $2 each. How many total action figures will he have by the end of the week?"""
    budget = 70
    days_for_wooden = 4
    wooden_price = 5
    wooden_spent = days_for_wooden * wooden_price
    plastic_budget = budget - wooden_spent
    days_for_plastic = 3
    plastic_price = 2
    plastic_quantity = plastic_budget // (plastic_price * days_for_plastic)
    wooden_quantity = days_for_wooden * wooden_price // wooden_price # This is just 4, but computed for consistency
    total_quantity = plastic_quantity + wooden_quantity
    result = total_quantity
    return result

print(solution())