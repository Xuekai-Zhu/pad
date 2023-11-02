def solution():
    
    john_age_when_john_was_19 = 19
    james_age_now = john_age_when_john_was_19 + (2 * john_age_when_john_was_19)
    james_age_in_3_years = james_age_now + 3
    youngest_son_age_at_32 = 32 - james_age_in_3_years
    result = youngest_son_age_at_32
    return result

print(solution())