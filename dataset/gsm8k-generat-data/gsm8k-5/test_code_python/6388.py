def solution():
    final_amount = 24  # Tim ends up with 24 cans of soda in the end
    jeff_took = 6  # Jeff takes 6 cans of soda from Tim
    remaining_amount = final_amount + jeff_took  # After Jeff took 6 cans, Tim had remaining cans left
    initial_amount = remaining_amount * 2  # Tim bought another half of the remaining amount

    result = initial_amount
    return result

print(solution())