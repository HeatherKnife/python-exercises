class Person:
    """docstring for Person"""
    def __init__(self, firstname, lastname):
        self.firstname = firstname
        self.lastname = lastname

    @classmethod
    def person_name(cls, lastname, firstname):
        print(firstname + " " + lastname)

class Student(Person):
	def __init__(self, firstname, lastname, subject_area):
		super().__init__(firstname, lastname)
		self.subject_area = subject_area

	@classmethod
	def student_name(cls, firstname, lastname, subject_area):
		print(firstname + " " + lastname + ", " + subject_area)
		
class Teacher(Person):
	def __init__(self, firstname, lastname, course):
		super().__init__(firstname, lastname)
		self.course = course

	@classmethod
	def teacher_name(cls, firstname, lastname, course):
		print(firstname + " " + lastname + ", " + course)

person = Person("Ana", "Gomez")
Person.person_name(person.lastname, person.firstname)
student = Student("Ana", "Gomez", "Nuclear physics")
Student.student_name(student.firstname, student.lastname, student.subject_area)
teacher = Teacher("Ana", "Gomez", "physics I")
Teacher.teacher_name(teacher.firstname, teacher.lastname, teacher.course)