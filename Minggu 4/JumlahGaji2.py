gajiPokok = {
    "Tetap": 1000000,
    "Honor": 750000
}

bonus = {
    "Tetap": {"A": 200000, "B": 400000, "C": 550000},
    "Honor": {"A": 150000, "B": 275000, "C": 480000}
}

for stat in ["Tetap", "Honor"]:
    print("Status", stat)
    for gol in ["A", "B", "C"]:
        print("Golongan", gol)
        print("Bonus", bonus.get(stat).get(gol))
        print("Gaji Total", gajiPokok.get(stat) + bonus.get(stat).get(gol))
        print()