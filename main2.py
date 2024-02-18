class Student:
    def __init__(self, grade, name):
        self.name = name
        self.grade = grade

    def study(self, hours):
        self.grade += hours

    def play(self, hours):
        self.grade -= hours * 0.05

    def get_grade(self):
        return self.grade


student = Student(6, "Вася")
lesson = float(input("Навчіть студента - "))
student.study(lesson)

game = float(input("Пограйте з студентом - "))
student.play(game)

grade = student.get_grade()

print(f"Оцінка студента {student.name}: {grade}")
