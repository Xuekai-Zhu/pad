def solution():
    starting_collection = 150

    grandpa_gift = 2 * uncle_gift
    uncle_gift = 5
    dad_gift = 10
    mum_gift = uncle_gift + 5
    auntie_gift = uncle_gift + 1

    total_gifts = grandpa_gift + uncle_gift + dad_gift + mum_gift + auntie_gift

    total_collection = starting_collection + total_gifts
    result = total_collection
    return result

print(solution())