def solution():
    elton_john = {"name": "Elton John", "profession": "pop singer", "knighted": True}
    tom_jones = {"name": "Tom Jones", "profession": "musician", "knighted": True}
    # Check if profession is related to knighthood
    if "musician" in elton_john["profession"] or "musician" in tom_jones["profession"]:
        result = "yes"
    else:
        result = "no"
    return result

print(solution())