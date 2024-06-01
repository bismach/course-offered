
class Course:
    def __init__(self, code, name):
        self.code = code
        self.name = name

    def __str__(self):
        return f"{self.code}: {self.name}"


class CourseCatalog:
    def __init__(self):
        self.courses = []

    def add_course(self, course):
        self.courses.append(course)
        print(f"Course '{course.name}' added successfully.")

    def view_courses(self):
        if not self.courses:
            print("No courses available.")
        else:
            print("Courses available:")
            for course in self.courses:
                print(course)


def main():
    catalog = CourseCatalog()

    while True:
        print("\nCourse Catalog Management System")
        print("1. Add Course")
        print("2. View Courses")
        print("3. Exit")
        choice = input("Enter your choice (1-3): ")

        if choice == '1':
            code = input("Enter course code: ")
            name = input("Enter course name: ")
            course = Course(code, name)
            catalog.add_course(course)
        elif choice == '2':
            catalog.view_courses()
        elif choice == '3':
            print("Exiting the system. Goodbye!")
            break
        else:
            print("Invalid choice, please try again.")

if __name__ == "__main__":
    main()
