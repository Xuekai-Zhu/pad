def solution():
    prohibited_items = ["drugs", "drug paraphernalia"]
    payment_platform = "Paypal"
    if any(item in prohibited_items for item in payment_platform):
        result = "unusual" # If Paypal prohibits drug-related items, it would be unusual to use it for drug deals
    else:
        result = "usual"
    return result

print(solution())