def calculate_grade(marks):
    if 90 <= marks <= 100:
        return "A", "Excellent! Keep shining ⭐"
    elif 80 <= marks <= 89:
        return "B", "Very Good! Keep it up! 👍"
    elif 70 <= marks <= 79:
        return "C", "Good job! You can do even better 🙂"
    elif 60 <= marks <= 69:
        return "D", "Needs improvement, keep practicing 💪"
    else:
        return "F", "Don't worry, try harder next time ❤️"


# Main Program
name = input("Enter student name: ")

while True:
    try:
        marks = int(input("Enter marks (0-100): "))
        if 0 <= marks <= 100:
            break
        else:
            print("❌ Invalid marks! Enter a number between 0 and 100.")
    except ValueError:
        print("❌ Please enter a valid number.")

grade, message = calculate_grade(marks)

print(f"\n📊 RESULT FOR {name.upper()}:")
print(f"Marks: {marks}/100")
print(f"Grade: {grade}")
print(f"Message: {message}")

