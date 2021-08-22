class Student:
    def __init__(self, name, surname, gender):
        self.name = name
        self.surname = surname
        self.gender = gender
        self.finished_courses = []
        self.courses_in_progress = []
        self.grades = {}
        
    def rate_lecturer(self, lecturer, course, grade):
        if isinstance(lecturer, Lecturer) and course in lecturer.courses_attached and course in self.courses_in_progress and grade <= 10:
            if course in lecturer.grades:
                lecturer.grades[course] += [grade]
            else:
                lecturer.grades[course] = [grade]
        else:
            return 'Ошибка' 

    def get_average_grade(self):
        sum_hw = 0
        count = 0
        for course in self.grades.values():
            sum_hw += sum(course)
            count += len(course)
            return round(sum_hw / count, 2)

    def __str__(self):
        res =(f'Имя: {self.name}\nФамилия: {self.surname}\nСредняя оценка за домашние задания: {self.get_average_grade()}\nКурсы в процессе изучения: {" ".join(self.courses_in_progress)}\nЗавершенные курсы: {" ".join(self.finished_courses)}')
        return res

    def __lt__(self, other_student):
        if not isinstance(other_student, Student):
            print('Такого студента нет')
            return
        else:
            return self.get_average_grade() < other_student.get_average_grade()        

class Mentor:
    def __init__(self, name, surname):
        self.name = name
        self.surname = surname
        self.courses_attached = []

class Reviewer(Mentor):
    def __init__(self, name, surname):
        super().__init__(name, surname)
        self.grades = {}

    def rate_hw(self, student, course, grade):
      if isinstance(student, Student) and course in self.courses_attached and course in student.courses_in_progress:
        if course in student.grades:
          student.grades[course] += [grade]
        else:
          student.grades[course] = [grade]
      else:
        return 'Ошибка'

    def __str__(self):
        res = (f'Имя: {self.name}\nФамилия: {self.surname}')
        return res

class Lecturer(Mentor):
    def __init__(self, name, surname):
        super().__init__(name, surname)
        self.grades = {}

    def get_average_grade(self):
        sum_lecturer = 0
        count = 0
        for course in self.grades.values():
            sum_lecturer += sum(course)
            count += len(course)
            return round(sum_lecturer / count, 2)
    
    def __str__(self):
        res = (f'Имя: {self.name}\nФамилия: {self.surname}\nСредняя оценка за лекции: {self.get_average_grade()}')
        return res
    
    def __lt__(self, other_lecturer):
        if not isinstance(other_lecturer, Lecturer):
            print('Такого лектора нет')
            return
        else:
            return self.get_average_grade() < other_lecturer.get_average_grade()  

def average_rating(student_list, course):
    total_sum = 0
    for student in student_list:
        for course_name, grades in student.grades.items():
            if course_name == course:
                total_sum += sum(grades) / len(grades)
    return round(total_sum / len(student_list), 2)

def average_rating_lecturer(lecturer_list, course):
    total_sum = 0
    for lecturer in lecturer_list:
        for course_name, grades in lecturer.grades.items():
            if course_name == course:
                total_sum += sum(grades) / len(grades)
    return round(total_sum / len(lecturer_list), 2)



student_1 = Student('Emma', 'Stone', 'Female')
student_1.courses_in_progress += ['Python']
student_1.courses_in_progress += ['Git']
student_1.finished_courses += ['Введение в программирование']

student_2 = Student('Jack', 'Nolan', 'Male')
student_2.courses_in_progress += ['Python']
student_2.courses_in_progress += ['Git']
student_2.finished_courses += ['Введение в программирование']

lecturer_1 = Lecturer('Nora', 'Trae')
lecturer_1.courses_attached += ['Python']
lecturer_1.courses_attached += ['Git']

lecturer_2 = Lecturer('Alex', 'Clare')
lecturer_2.courses_attached += ['Python']
lecturer_2.courses_attached += ['Git']

reviewer_1 = Reviewer('Some', 'Buddy')
reviewer_1.courses_attached += ['Python']
reviewer_1.courses_attached += ['Git']

reviewer_1.rate_hw(student_1, 'Python', 10)
reviewer_1.rate_hw(student_1, 'Python', 7)
reviewer_1.rate_hw(student_1, 'Git', 8)
reviewer_1.rate_hw(student_1, 'Git', 9)
reviewer_1.rate_hw(student_1, 'Git', 7)
reviewer_1.rate_hw(student_2, 'Python', 8)
reviewer_1.rate_hw(student_2, 'Python', 6)
reviewer_1.rate_hw(student_2, 'Git', 7)
reviewer_1.rate_hw(student_2, 'Git', 6)
reviewer_1.rate_hw(student_2, 'Git', 7)

reviewer_2 = Reviewer('Rita', 'Pale')
reviewer_2.courses_attached += ['Python']
reviewer_2.courses_attached += ['Git']

reviewer_2.rate_hw(student_1, 'Python', 9)
reviewer_2.rate_hw(student_1, 'Python', 10)
reviewer_2.rate_hw(student_1, 'Git', 10)
reviewer_2.rate_hw(student_1, 'Git', 7)
reviewer_2.rate_hw(student_1, 'Git', 9)
reviewer_2.rate_hw(student_2, 'Python', 7)
reviewer_2.rate_hw(student_2, 'Python', 7)
reviewer_2.rate_hw(student_2, 'Git', 8)
reviewer_2.rate_hw(student_2, 'Git', 5)
reviewer_2.rate_hw(student_2, 'Git', 6)

student_1.rate_lecturer(lecturer_1, 'Python', 9)
student_1.rate_lecturer(lecturer_1, 'Git', 10)
student_1.rate_lecturer(lecturer_2, 'Python', 8)
student_1.rate_lecturer(lecturer_2, 'Git', 7)

student_2.rate_lecturer(lecturer_1, 'Python', 10)
student_2.rate_lecturer(lecturer_1, 'Git', 9)
student_2.rate_lecturer(lecturer_2, 'Python', 7)
student_2.rate_lecturer(lecturer_2, 'Git', 7)

print(student_1.grades)
print(student_2.grades)

print(student_1)
print(student_2)

print(student_1 > student_2)

print(lecturer_1 > lecturer_2)

print(lecturer_1)
print(reviewer_2)

print(average_rating([student_1, student_2], 'Python'))

print(average_rating_lecturer([lecturer_1, lecturer_2], 'Python'))
