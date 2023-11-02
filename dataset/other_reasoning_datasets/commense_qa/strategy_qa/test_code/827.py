def solution():
    has_anorexia_nervosa = True
    at_high_risk_for_osteoporosis = True
    if has_anorexia_nervosa and at_high_risk_for_osteoporosis:
        result = "yes"
    else:
        result = "no"
    return result

print(solution())