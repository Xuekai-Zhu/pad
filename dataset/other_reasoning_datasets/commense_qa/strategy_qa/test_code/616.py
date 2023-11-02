def solution():
    required_degrees = ["engineering", "biological science", "physical science", "mathematics"]
    stephen_king_degree = "English"
    if stephen_king_degree in required_degrees:
        result = "no"
    else:
        result = "yes"
    return result

print(solution())