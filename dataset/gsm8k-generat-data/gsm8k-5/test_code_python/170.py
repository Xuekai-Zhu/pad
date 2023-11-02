def solution():
    katherine_age = 24  # Katherine will be 24 years old
    mel_age = katherine_age - 3  # Mel is three years younger than Katherine
    years_until_katherine_turns_24 = katherine_age - mel_age  # Mel has to wait this many years before Katherine turns 24
    mel_age_when_katherine_is_24 = mel_age + years_until_katherine_turns_24  # Mel will be this old when Katherine is 24

    result = mel_age_when_katherine_is_24
    return result

print(solution())