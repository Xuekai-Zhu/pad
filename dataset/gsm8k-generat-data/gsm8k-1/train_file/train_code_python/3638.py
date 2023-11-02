def solution():
    """
    A small pizza can gives 4 slices, and a large pizza gives 8 slices. George purchased 
    3 small and 2 large pizzas. George would like to eat 3 pieces. His friend Bob 
    would like to eat one more piece than George. Susie will eat half as many as Bob. 
    Bill, Fred and Mark would each like 3 pieces. How many slices of pizza will be left over?
    """
    small_pizza = 4
    large_pizza = 8
    george_slices = 3
    bob_slices = george_slices + 1
    susie_slices = bob_slices / 2
    bill_slices = 3
    fred_slices = 3
    mark_slices = 3
    total_slices = (3 * small_pizza) + (2 * large_pizza)
    total_slices -= (george_slices + bob_slices + susie_slices 
                     + bill_slices + fred_slices + mark_slices)
    result = total_slices
    return result

print(solution())