def solution():
    # Define initial collection and gift amounts
    initial_collection = 150
    grandpa_gift = 2 * uncle_gift
    dad_gift = mum_gift - 5
    auntie_gift = uncle_gift + 1

    # Calculate total gift amount
    total_gifts = grandpa_gift + uncle_gift + dad_gift + auntie_gift

    # Calculate total collection after receiving gifts
    final_collection = initial_collection + total_gifts
    result = final_collection
    return result

print(solution())