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
        
    def get_avg_grade(self):
        avg_grade = round(float(sum(self.grades.values()) / len(self.grades.values())), 1)
        return avg_grade

    def __str__(self):
        output_1 = f'Имя: {self.name}\nФамилия: {self.surname}\nСредняя оценка за домашние задания: {self.get_avg_grade()}\n'
        output_2 = f'Курсы в процессе изучения: {self.courses_in_progress}\nЗавершённые курсы: {self.finished_courses}\n'
        return output_1 + output_2
    
    def __lt__(self, other):
        if not isinstance(other, Student):
           return 'Not a student'            
        return self.get_avg_grade() < other.get_avg_grade()
    
    def get_grades_by_lecturers(self, Lecturers_list, Course_name):
        avg_grades = {} 
        for lecturer in Lecturers_list:
            if Course_name not in lecturer.courses_attached:
                avg_grades[lecturer.name + ' ' + lecturer.surname] = 'Не ведёт этот курс'
            else:
                avg_grades[lecturer.name + ' ' + lecturer.surname] = lecturer.get_avg_grade()
        return avg_grades
    
    
class Mentor:
    def __init__(self, name, surname):
        self.name = name
        self.surname = surname
        self.courses_attached = []
        self.grades = {}

    def get_grades_by_students(self, Students_list, Course_name):
        avg_grades = {} 
        for student in Students_list:
            if Course_name not in student.courses_in_progress:
                avg_grades[student.name + ' ' + student.surname] = 'Курс не изучен'
            else:
                avg_grades[student.name + ' ' + student.surname] = student.get_avg_grade()
        return avg_grades

class Lecturer(Mentor):     
    def get_avg_grade(self):
        avg_grade = round(float(sum(self.grades.values()) / len(self.grades.values())), 1)
        return avg_grade

    def __str__(self):
        output = f'Имя: {self.name}\nФамилия: {self.surname}\nСредняя оценка за лекции: {self.get_avg_grade()}\n'
        return output
    
    def __lt__(self, other):
        if not isinstance(other, Lecturer):
            return 'Not a lecturer'
        return self.get_avg_grade() < other.get_avg_grade()

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
        output = f'Имя: {self.name}\nФамилия: {self.surname}\n'
        return output
       
first_student = Student('Eric', 'Cartman', 'Piggy')
first_student.finished_courses += ['Gender Science', 'Maths', 'Spanish']
first_student.courses_in_progress += ['Psychology', 'Personal Safety', 'Other Stuff']

second_student = Student('Kyle', 'Broflovsky', 'Ginger')
second_student.finished_courses += ['Maths', 'Personal Safety', 'Other Stuff']
second_student.courses_in_progress += ['Gender Science', 'Spanish', 'Psychology']

first_lecturer = Lecturer('Mr./Mrs.', 'Garrison')
first_lecturer.courses_attached += ['Gender Science', 'Maths', 'Other Stuff']
second_lecturer = Lecturer('Mr.', 'Mackey')
second_lecturer.courses_attached += ['Spanish', 'Psychology', 'Personal Safety']

first_student.rate_lecturer(first_lecturer, 'Gender Science', 10)
first_student.rate_lecturer(first_lecturer, 'Maths', 5)
second_student.rate_lecturer(first_lecturer, 'Maths', 4)
second_student.rate_lecturer(first_lecturer, 'Other Stuff', 7)
first_student.rate_lecturer(second_lecturer, 'Spanish', 7)
second_student.rate_lecturer(second_lecturer, 'Personal Safety', 3)

first_reviewer = Reviewer('Chef', 'Chef')
first_reviewer.courses_attached += ['Personal Safety', 'Other Stuff', 'Spanish']
first_reviewer.rate_student(first_student, 'Personal Safety', 8)
first_reviewer.rate_student(first_student, 'Other Stuff', 7)
first_reviewer.rate_student(second_student, 'Spanish', 3)

second_reviewer = Reviewer('Mr.', 'Slave')
second_reviewer.courses_attached += ['Maths', 'Psychology', 'Gender Science']
second_reviewer.rate_student(first_student, 'Psychology', 9)
second_reviewer.rate_student(first_student, 'Gender Science', 6)
second_reviewer.rate_student(second_student, 'Psychology', 4)

print(first_student)
print(second_student)
print(first_lecturer)
print(second_lecturer)
print(first_reviewer)
print(second_reviewer)
print(first_student < second_student)
print(first_lecturer > second_lecturer)
print(first_student < second_lecturer)
print(first_lecturer < second_student)

stud_list = [first_student, second_student]
print(first_reviewer.get_grades_by_students(stud_list, 'Psychology'))
lect_list = [first_lecturer, second_lecturer]
print(first_student.get_grades_by_lecturers(lect_list, 'Gender Science'))