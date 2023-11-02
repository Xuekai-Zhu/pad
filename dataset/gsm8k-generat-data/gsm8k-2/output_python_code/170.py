def solution():
    """Mel is three years younger than Katherine. When Katherine is two dozen years old, how old will Mel be in years?"""
    katherine_age = 24
    mel_age = katherine_age - 3
    years_to_go = katherine_age - mel_age
    mel_future_age = katherine_age + years_to_go
    result = mel_future_age
    return result

print(solution())