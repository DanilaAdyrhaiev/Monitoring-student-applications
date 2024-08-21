import os
import openpyxl
from education import UniversityService, Faculty, Student

class ExcelWriter:
    def __init__(self, university_service: UniversityService):
        self.university_service = university_service

    def write_to_excel(self) -> None:
        filename = "University.xlsx"

        if not os.path.exists(filename):
            workbook = openpyxl.Workbook()
        else:
            workbook = openpyxl.load_workbook(filename)

        universities = self.university_service.get_all()

        for university_name, university in universities.items():
            for faculty_name, faculty in university.faculties.items():
                sheet_name = f"{university_name[:10]}-{faculty_name[:10]}-{faculty.program[:10]}"
                
                sheet_name = sheet_name[:31]
                original_sheet_name = sheet_name
                suffix = 1
                while sheet_name in workbook.sheetnames:
                    sheet_name = f"{original_sheet_name[:28]}_{suffix}"
                    suffix += 1
                
                
                if sheet_name in workbook.sheetnames:
                    sheet = workbook[sheet_name]  
                    sheet.delete_rows(1, sheet.max_row)  
                else:
                    sheet = workbook.create_sheet(title=sheet_name)  
                
                row = 1
            
                sheet.merge_cells(start_row=row, start_column=1, end_row=row, end_column=3)
                sheet.cell(row=row, column=1, value=f"Университет: {university_name}")
                row += 1

                sheet.merge_cells(start_row=row, start_column=1, end_row=row, end_column=3)
                sheet.cell(row=row, column=1, value=f"Факультет: {faculty_name}")
                row += 1

                sheet.merge_cells(start_row=row, start_column=1, end_row=row, end_column=3)
                sheet.cell(row=row, column=1, value=f"Программа: {faculty.program}")
                row += 1

                # Заголовки для студентов
                sheet.cell(row=row, column=1, value="№")
                sheet.cell(row=row, column=2, value="ФИО")
                sheet.cell(row=row, column=3, value="Бал")
                row += 1

                for index, student in enumerate(faculty.students, start=1):
                    sheet.cell(row=row, column=1, value=index)
                    sheet.cell(row=row, column=2, value=student.name)
                    sheet.cell(row=row, column=3, value=student.rating)
                    row += 1

        # Удаляем пустой стандартный лист
        if 'Sheet' in workbook.sheetnames:
            del workbook['Sheet']
        workbook.save(filename)
