def solution():
    latin_alphabet = ["A", "B", "C", "D", "E", "F", "G", "H", "I", "J", "K", "L", "M", "N", "O", "P", "Q", "R", "S", "T", "U", "V", "W", "X", "Y", "Z"]
    ancient_phonician_alphabet = ["Aleph", "Bet", "Gimel", "Dalet", "He", "Vav", "Zayin", "Het", "Tet", "Yod", "Kaf", "Lamed", "Mem", "Nun", "Samekh", "Ayin", "Pe", "Tsadi", "Qof", "Resh", "Shin", "Taw"]
    dalet_glyph = "\u05DA"
    if latin_alphabet.index("D") == ancient_phonician_alphabet.index("Dalet") and dalet_glyph in ancient_phonician_alphabet:
        result = "yes"
    else:
        result = "no"
    return result

print(solution())