#Question3
name = input("Enter your name: ")
lab_grade= float(input("Enter the lab grade: "))
midterm_grade=float(input("Enter the midterm grade: "))
final_grade=float(input("Enter the final grade: "))

last_score = lab_grade*0.25 + midterm_grade*0.35 + final_grade*0.4
print("Name : " , name)
print("Lab: " , lab_grade)
print("Midterm : " , midterm_grade)
print("Final : " , final_grade)
print("Last Score : " , last_score)

