from ExcelWriter import ExcelWriter
from ApplicationChecker import CheckMyUniversity

def main() -> None:
    univers = [
        'https://vstup.osvita.ua/y2024/r27/183/1336336/',
        'https://vstup.osvita.ua/y2024/r27/174/1303221/',
        'https://vstup.osvita.ua/y2024/r27/174/1308110/',
        'https://vstup.osvita.ua/y2024/r27/79/1295330/'
    ]
    
    # Получаем данные университетов и факультетов
    university_service = CheckMyUniversity(univers)
    
    # Инициализируем MultiSheetExcelWriter с университетским сервисом
    excel_writer = ExcelWriter(university_service)
    
    # Создаём один файл Excel с несколькими листами
    excel_writer.write_to_single_excel_file()
    
    print("Done")

if __name__ == "__main__":
    main()
