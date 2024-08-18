class Student:
    def __init__(self, name: str) -> None:
        self.__name: str = name

    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, name: str) -> None:
        self.__name = name


class StudentService:
    def __init__(self, students: list[Student] = None) -> None:
        self.__students = students or []

    @property
    def students(self) -> list[Student]:
        return self.__students

    @students.setter
    def students(self, students: list[Student]) -> None:
        self.__students = students

    def add_student(self, student: Student) -> None:
        self.__students.append(student)

    def find_student(self, name: str) -> Student:
        for student in self.__students:
            if student.name == name:
                return student
        return None


class Faculty:
    def __init__(self, name: str, program: str, students: list[Student] = None) -> None:
        self.__name: str = name
        self.__program: str = program
        self.__students: list[Student] = students or []

    @property
    def name(self) -> str:
        return self.__name

    @property
    def program(self) -> str:
        return self.__program

    @property
    def students(self) -> list[Student]:
        return self.__students

    @program.setter
    def program(self, program: str) -> None:
        self.__program = program

    @students.setter
    def students(self, students: list[Student]) -> None:
        self.__students = students


class FacultyService:
    def __init__(self, faculties: dict[str, Faculty] = None) -> None:
        self.__faculties = faculties or {}

    @property
    def faculties(self) -> dict[str, Faculty]:
        return self.__faculties

    @faculties.setter
    def faculties(self, faculties: dict[str, Faculty]) -> None:
        self.__faculties = faculties

    def add_faculty(self, faculty: Faculty) -> None:
        self.__faculties[faculty.name] = faculty

    def find_faculty(self, name: str) -> Faculty:
        return self.__faculties.get(name)


class University:
    def __init__(self, title: str, faculties: list[Faculty] = None) -> None:
        self.__title: str = title
        self.__faculties: list[Faculty] = faculties or []

    @property
    def title(self) -> str:
        return self.__title

    @property
    def faculties(self) -> list[Faculty]:
        return self.__faculties

    @title.setter
    def title(self, title: str) -> None:
        self.__title = title

    @faculties.setter
    def faculties(self, faculties: list[Faculty]) -> None:
        self.__faculties = faculties


class UniversityService:
    def __init__(self, universities: dict[str, University] = None) -> None:
        self.__universities = universities or {}

    @property
    def universities(self) -> dict[str, University]:
        return self.__universities

    @universities.setter
    def universities(self, universities: dict[str, University]) -> None:
        self.__universities = universities

    def add_university(self, university: University) -> None:
        self.__universities[university.title] = university

    def find_university(self, title: str) -> University:
        return self.__universities.get(title)
