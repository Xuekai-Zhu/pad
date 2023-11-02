def solution():
    # Calculate the amount of wax used for detailing car and SUV
    wax_used = 3 + 4  # 3 ounces to detail car and 4 ounces to detail SUV

    # Calculate the amount of wax left after spilling and detailing
    remaining_wax = 11 - 2 - wax_used  # 11 ounces bought, 2 ounces spilled, wax_used ounces used

    result = remaining_wax
    return result

print(solution())