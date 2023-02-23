class Student:
    def __init__(self, name, surname, gender):
        self.name = name
        self.surname = surname
        self.gender = gender
        self.finished_courses = []
        self.courses_in_progress = []
        self.grades = {}

    def add_courses(self, course_name):
        self.finished_courses.append(course_name)

    def rate_lecturer(self, lecturer, course, grade):
        if isinstance(lecturer, Lecturer) and course in self.finished_courses and course in lecturer.courses_attached and grade in range(11):
            if course in lecturer.grades:
                lecturer.grades[course] += grade
            else:
                lecturer.grades[course] = grade
        else:
            return 'Ошибка: данные лектора, студента или оценки введены некорректно'

    def __str__(self):
        output_1 = f'Имя: {self.name}\nФамилия: {self.surname}\nСредняя оценка за домашние задания: {float(sum(self.grades.values()) / len(self.grades.values()))}\n'
        output_2 = f'Курсы в процессе изучения: {self.courses_in_progress}\nЗавершённые курсы: {self.finished_courses}\n'
        return output_1 + output_2
        
class Mentor:
    def __init__(self, name, surname):
        self.name = name
        self.surname = surname
        self.courses_attached = []

class Lecturer(Mentor):
    grades = {}
        
    def __str__(self):
        output = f'Имя: {self.name}\nФамилия: {self.surname}\nСредняя оценка за лекции: {float(sum(self.grades.values()) / len(self.grades.values()))}\n'
        return output

class Reviewer(Mentor):
    def rate_student(self, student, course, grade):
        if isinstance(student, Student) and course in self.courses_attached and course in student.courses_in_progress and grade in range(11):
            if course in student.grades:
                student.grades[course] += grade
            else:
                student.grades[course] = grade
        else:
            return 'Ошибка: данные лектора, студента или оценки введены некорректно'

    def __str__(self):
        output = f'Имя: {self.name}\nФамилия: {self.surname}'
        return output

some_student = Student('Someone', 'Unknown', 'gender_fluid')
some_student.finished_courses += ['Quantum_physics', 'Public relations', 'Geometry']
some_student.courses_in_progress += ['Theology', 'Necromancy']

awesome_lecturer = Lecturer('Stephen', 'Hawking')
awesome_lecturer.courses_attached += ['Quantum_physics', 'Public relations', 'Geometry']
some_student.rate_lecturer(awesome_lecturer, 'Quantum_physics', 10)
some_student.rate_lecturer(awesome_lecturer, 'Public relations', 8)
some_student.rate_lecturer(awesome_lecturer, 'Geometry', 9)

filthy_reviewer = Reviewer('Dolores', 'Umbridge')
filthy_reviewer.courses_attached += ['Theology', 'Necromancy']
filthy_reviewer.rate_student(some_student, 'Theology', 3)
filthy_reviewer.rate_student(some_student, 'Necromancy', 5)

print(some_student)
print(awesome_lecturer)
print(filthy_reviewer)
