ar=int(input("Mennyi a termék jelenlegi ára: "))
szaz=int(input("Mekkora az árcsökkentés: "))

print(f"A termék új ára: {ar - (szaz/100) * ar} FT")