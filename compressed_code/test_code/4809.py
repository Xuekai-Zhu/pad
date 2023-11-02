def solution():
    
    total_bears = 20
    daragh_fav = 8
    remaining_bears = total_bears - daragh_fav
    other_sisters_bears = remaining_bears / 3
    eden_bears = other_sisters_bears + 10
    result = eden_bears
    return result

print(solution())