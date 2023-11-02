def solution():
    james_years = 20
    john_years_ago = (james_years - 8) * 2
    john_years = john_years_ago + 8
    mike_years = john_years - 16
    combined_experience = james_years + john_years + mike_years
    result = combined_experience
    return result

print(solution())