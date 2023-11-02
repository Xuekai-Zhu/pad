def solution():
    stores = {"Casio": "consumer electronics and watches", "Petco": "pet supplies"}
    casio_products = stores["Casio"]
    petco_products = stores["Petco"]
    if casio_products in petco_products:
        result = "yes"
    else:
        result = "no"
    return result

print(solution())