def solution():
    glasses_improve_vision = True
    qr_codes_not_readable_by_humans = True
    if qr_codes_not_readable_by_humans and not glasses_improve_vision:
        result = "no"
    else:
        result = "yes"
    return result

print(solution())