import os

LINE = "last 1% confession: i knew exactly what u meant every time i typed duck, ur photos were never backed up, and tiktok killed me. tell the charger i lo"


def main():
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(LINE)


if __name__ == "__main__":
    main()
