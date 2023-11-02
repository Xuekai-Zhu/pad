def solution():
    astronaut_degrees = ["engineering", "biological science", "physical science", "computer science", "mathematics"]
    danica_degree = "mathematics"
    if danica_degree in astronaut_degrees:
        result = "yes"
    else:
        result = "no"
    return result

print(solution())