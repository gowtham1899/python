class Student:
    def __init__(self, name, grade):
        self.name = name
        self.__grade = grade  # encapsulated

    def get_grade(self):
        return self.__grade

    def set_grade(self, new_grade):
        if 0 <= new_grade <= 100:
            self.__grade = new_grade
        else:
            print("Invalid grade!")

    def display_info(self):
        print(f"Name: {self.name}, Grade: {self.__grade}")

# Function to manage students
def manage_students():
    s1 = Student("Alice", 85)
    s2 = Student("Bob", 92)

    s1.display_info()
    s2.display_info()

    s1.set_grade(95)
    print("After updating grade:")
    s1.display_info()

manage_students()
