import os
import openpyxl
from education import UniversityService, Faculty, Student

class ExcelWriter:
    def __init__(self, university_service: UniversityService):
        self.university_service = university_service

    def write_to_excel(self) -> None:
        filename = "University.xlsx"

        # Проверяем, существует ли файл
        if not os.path.exists(filename):
            workbook = openpyxl.Workbook()  # Создаём новую книгу
        else:
            workbook = openpyxl.load_workbook(filename)  # Загружаем существующую

        universities = self.university_service.get_all()

        for university_name, university in universities.items():
            if university_name[:31] in workbook.sheetnames:
                sheet = workbook[university_name[:31]]  # Если лист существует, обновляем его
            else:
                sheet = workbook.create_sheet(title=university_name[:31])  # Создаём новый лист
            
            row = 1
            # Запись названия университета
            sheet.merge_cells(start_row=row, start_column=1, end_row=row, end_column=3)
            sheet.cell(row=row, column=1, value=f"Университет: {university_name}")
            row += 1

            for faculty_name, faculty in university.faculties.items():
                # Запись названия факультета
                sheet.merge_cells(start_row=row, start_column=1, end_row=row, end_column=3)
                sheet.cell(row=row, column=1, value=f"Факультет: {faculty_name}")
                row += 1

                # Запись программы
                sheet.merge_cells(start_row=row, start_column=1, end_row=row, end_column=3)
                sheet.cell(row=row, column=1, value=f"Программа: {faculty.program}")
                row += 1

                # Заголовки для студентов
                sheet.cell(row=row, column=1, value="№")
                sheet.cell(row=row, column=2, value="ФИО")
                sheet.cell(row=row, column=3, value="Бал")
                row += 1

                # Запись студентов
                for index, student in enumerate(faculty.students, start=1):
                    sheet.cell(row=row, column=1, value=index)
                    sheet.cell(row=row, column=2, value=student.name)
                    sheet.cell(row=row, column=3, value=student.rating)
                    row += 1
                
                # Пропуск строки перед следующим факультетом
                row += 1

        # Удаляем пустой стандартный лист, если он существует
        if 'Sheet' in workbook.sheetnames:
            del workbook['Sheet']

        # Сохраняем книгу
        workbook.save(filename)
