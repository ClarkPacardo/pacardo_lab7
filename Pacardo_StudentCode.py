name = str(input("Enter your name: "))
section = str(input("Enter your Section: "))
prelim = float(input("Prelim Grade: "))
midterm = float(input("Midterm Grade: "))
final = float(input("Final Grade: "))
ave_grade = round(prelim * 0.333)+(midterm * 0.333)+(final * 0.333)
print(ave_grade)

if prelim <= 40:
    print("Invalid Input")
if midterm <= 40:
    print("Invalid Input")
if final <= 40:
    print("Invalid Input")
    
if ave_grade <= 100 and ave_grade >= 99:
    print(name, "from", section, "Your GPA is 1.00")
elif ave_grade <= 98 and ave_grade >= 96:
    print(name, "from", section, "Your GPA is 1.25")
elif ave_grade <= 95 and ave_grade >= 93:
    print(name, "from", section, "Your GPA is 1.50")
elif ave_grade <= 92 and ave_grade >= 90:
    print(name, "from", section, "Your GPA is 1.75")
elif ave_grade <= 89 and ave_grade >= 87:
    print(name, "from", section, "Your GPA is 2.00")
elif ave_grade <= 86 and ave_grade >= 84:
    print(name, "from", section, "Your GPA  is 2.25")
elif ave_grade <= 83 and ave_grade >= 81:
    print(name, "from", section, "Your GPA  is 2.50")
elif ave_grade <= 80 and ave_grade >= 78:
    print(name, "from", section, "Your GPA  is 2.75")
elif ave_grade <= 77 and ave_grade >= 75:
    print(name, "from", section, "Your GPA  is 3.00")
elif ave_grade <= 74 and ave_grade >= 40:
    print(name, "from", section, "Your GPA is 5.00")
else:
    print("Invalid Input")