def solution():
    money = 300
    rose_price = 2
    Jenna_fraction = 1/3
    Imma_fraction = 1/2
    total_fraction = Jenna_fraction + Imma_fraction
    number_of_roses = money / rose_price
    number_of_roses_for_friends = number_of_roses * total_fraction
    result = number_of_roses_for_friends
    return result

print(solution())