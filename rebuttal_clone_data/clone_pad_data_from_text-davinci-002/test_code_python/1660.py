def solution():
    total_papayas = 14
    papayas_on_friday = total_papayas - 2
    papayas_on_sunday = papayas_on_friday - (2 * papayas_on_friday)
    result = papayas_on_sunday
    return result

print(solution())