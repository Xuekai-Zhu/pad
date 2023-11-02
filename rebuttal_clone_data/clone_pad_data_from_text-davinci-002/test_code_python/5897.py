def solution():
    initial_collection = 150
    gift_grandpa = 2 * initial_collection
    gift_uncle = initial_collection / 2
    gift_dad = 10
    gift_mum = gift_dad + 5
    gift_auntie = gift_uncle + 1
    total_gift = gift_grandpa + gift_uncle + gift_dad + gift_mum + gift_auntie
    total_collection = initial_collection + total_gift
    result = total_collection
    return result

print(solution())