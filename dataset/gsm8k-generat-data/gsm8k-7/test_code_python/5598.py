def solution():
    mary_towels = 24
    mary_weight = mary_towels * 2.5  # Assuming each towel weighs 2.5 pounds
    total_weight = 60
    francis_towels = mary_towels / 4  # Given that Mary has 4 times as many towels as Frances
    francis_weight = (total_weight - mary_weight) / 16  # Convert pounds to ounces

    result = francis_weight
    return result

print(solution())