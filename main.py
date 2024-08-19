from ExcelWriter import ExcelWriter
from ApplicationChecker import CheckMyUniversity

def main() -> None:
    univers = [
    'https://vstup.osvita.ua/y2024/r27/183/1336336/',
    'https://vstup.osvita.ua/y2024/r27/174/1303221/',
    'https://vstup.osvita.ua/y2024/r27/174/1308110/',
    'https://vstup.osvita.ua/y2024/r27/79/1295330/'
    ]
    ExcelWriter(CheckMyUniversity(univers)).write_to_excel()
    print("Done")


if __name__ == "__main__":
    main()