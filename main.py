# Задание № 3. Полиморфизм и магические методы
# Перегрузите магический метод __str__ у всех классов.
# У проверяющих он должен выводить информацию в следующем виде:

class Student:
    def __init__(self, name, surname, gender, avg_grade, courses_in_progress, finished_courses):
        self.name = name
        self.surname = surname
        self.gender = gender
        self.finished_courses = []
        self.courses_in_progress = []
        self.grades = {}
        self.avg_grade = avg_grade

    def rate_lec(self, lecturer, course, grade):
        if isinstance(lecturer,
                      Lecturer) and course in self.courses_in_progress and course in lecturer.courses_attached:
            if course in lecturer.grades:
                lecturer.grades[course] += [grade]
            else:
                lecturer.grades[course] = [grade]

        else:
            return 'Error'

    def __str__(self):
        self.courses_in_progress = 'Python, Git'
        self.finished_courses = 'Введение в программирование'
        res_st = f'Имя: {self.name}\nФамилия: {self.surname}\nСредняя оценка за домашние задания: {self.avg_grade}\n' \
                 f'Курсы в процессе изучения: {self.courses_in_progress}\nЗавершенные курсы: {self.finished_courses}'
        return res_st

    def __lt__(self, other):
        if not isinstance(other, Student):
            print('Not a Student')
            return
        return self.avg_grade < other.avg_grade


class Mentors:
    def __init__(self, name, surname):
        self.name = name
        self.surname = surname
        self.courses_attached = []


class Lecturer(Mentors):
    def __init__(self, name, surname, avg_grade):
        super().__init__(name, surname)
        self.grades = {}
        self.avg_grade = avg_grade

    def __str__(self):
        res_lec = f'Имя: {self.name}\nФамилия: {self.surname}\nСредняя оценка за лекции: {self.avg_grade}'
        return res_lec

    def __lt__(self, other):
        if not isinstance(other, Lecturer):
            print('Not a Lecturer')
            return
        return self.avg_grade < other.avg_grade


class Reviewer(Mentors):
    def rate_st(self, student, course, grade):
        if isinstance(student, Student) and course in self.courses_attached and course in student.courses_in_progress:
            if course in student.grades:
                student.grades[course] += [grade]
            else:
                student.grades[course] = [grade]

        else:
            return 'Error'

    def __str__(self):
        res_rev = f'Имя: {self.name}\nФамилия: {self.surname}'
        return res_rev

some_reviewers = Reviewer('Some', 'Buddy')
some_lecturer = Lecturer('Some', 'Buddy', 9.9)
some_student = Student('Ruoy', 'Eman', 'your_gender', 9.9, 'Python, Git', 'Введение в программирование')
print(some_reviewers)
print()
print(some_lecturer)
print()
print(some_student)
print()
