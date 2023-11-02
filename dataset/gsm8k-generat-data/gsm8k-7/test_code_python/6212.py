def solution():
    starting_bears = 20
    favorite_bears = 8
    remaining_bears = starting_bears - favorite_bears
    sisters = 3
    eden_start = 10

    # Divide the remaining bears equally among Daragh's 3 sisters
    split_bears = remaining_bears // sisters

    # Eden's total number of stuffed bears is her initial number plus her share of the remaining bears
    eden_total = eden_start + split_bears

    result = eden_total
    return result

print(solution())