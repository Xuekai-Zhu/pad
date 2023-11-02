def solution():
    available_money = 300
    rose_price = 2
    num_roses = available_money // rose_price

    # Calculate number of roses for Jenna and Imma
    num_roses_jenna = num_roses // 3
    num_roses_imma = num_roses // 2

    # Calculate total number of roses given to friends
    total_roses = num_roses_jenna + num_roses_imma
    result = total_roses
    return result

print(solution())