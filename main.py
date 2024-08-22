from ExcelWriter import ExcelWriter
from ApplicationChecker import CheckMyUniversity

def main() -> None:
    univers = [
        'https://vstup.osvita.ua/y2024/r27/183/1336336/',
        'https://vstup.osvita.ua/y2024/r27/41/1350186/',
        'https://vstup.osvita.ua/y2024/r27/41/1292166/',
        'https://vstup.osvita.ua/y2024/r27/41/1300345/',
        'https://vstup.osvita.ua/y2024/r27/174/1308501/',
        'https://vstup.osvita.ua/y2024/r27/174/1303052/',
        'https://vstup.osvita.ua/y2024/r27/174/1308500/',
        'https://vstup.osvita.ua/y2024/r27/174/1335188/',
        'https://vstup.osvita.ua/y2024/r27/79/1295330/'
        
    ]
    
    university_service = CheckMyUniversity(univers)
    excel_writer = ExcelWriter(university_service)
    excel_writer.write_to_excel()
    
    print("Done")

if __name__ == "__main__":
    main()
