class Student:

  def __init__(self, name, roll_number, cgpa):
    self.name= name
    self. roll_number= roll_number
    self.cgpa= cgpa


def sort_students(students_list):
  sort_students= sorted(students_list, key=lambda student: student.cgpa, reverse= True)
  return sort_students

students= [
  Student("Sana", "A123", 9.0),
  Student("Padma", "A124", 8.0),
  Student("Sowndarya", "A125", 9.5),
  Student("Raghavi", "A126", 9.0),
]

sorted_students= sort_students(students)

for student in sorted_students:
  print("Name:{}, Roll Number:{}, CGPA:{}".format(student.name, student.roll_number,
                                                  student.cgpa))
  