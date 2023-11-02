def solution():

    Tiffany_blocks_per_minute = 6/3
    Moses_blocks_per_minute = 12/8
    if Tiffany_blocks_per_minute > Moses_blocks_per_minute:
        result = Tiffany_blocks_per_minute
    else:
        result = Moses_blocks_per_minute
    return result

Question: Jennie spends 3/8 of her time on the phone, 1/4 of her time doing laundry, and the rest of her time she is either sleeping or doing other things.  Jennie spends a total of 56 hours awake each week.  How many hours does Jennie spend on the phone each week?
Answer:
def solution():

    time_on_phone = 3/8
    time_on_laundry = 1/4
    time_awake = 56
    time_other = time_awake - (time_on_phone + time_on_laundry)
    result = time_on_phone * time_awake
    return result

print(solution())