def solution():
    signature_style = ["oversized pullover sweater", "thigh high heels"]
    comfort_items = ["oversized pullover sweater"]
    high_fashion_items = ["thigh high heels"]
    if all(item in signature_style for item in comfort_items) and all(item in signature_style for item in high_fashion_items):
        result = "yes"
    else:
        result = "no"
    return result

print(solution())