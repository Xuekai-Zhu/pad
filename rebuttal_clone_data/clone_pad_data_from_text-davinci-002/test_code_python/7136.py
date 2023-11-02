def solution():
    cookies_made = 4
    dozen_cookie = cookies_made * 12
    chips_per_cookie = 7
    total_chips = chips_per_cookie * dozen_cookie
    uneaten_cookies = total_chips / 2
    uneaten_chips = uneaten_cookies * chips_per_cookie
    result = uneaten_chips
    return result

print(solution())