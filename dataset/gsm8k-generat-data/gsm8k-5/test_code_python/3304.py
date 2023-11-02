def solution():
    apples = 15  # There are 15 apples in the basket
    oranges = apples // 4  # There are four times as many apples as oranges
    total_fruits = apples + oranges  # Calculate the total number of fruits in the basket
    amount_to_eat = 2/3  # Emiliano eats 2/3 of each fruit's quantity in the basket

    # Calculate the number of fruits Emiliano would have consumed
    consumed_fruits = total_fruits * amount_to_eat
    result = consumed_fruits
    return result

print(solution())