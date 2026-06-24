subjects = ["Mathematics", "Science", "English", "Computer Science"]

print("\nLet's calculate your grades")
print("Enter your marks out of 100 for each subject.\n")

marks = []
for subject in subjects:
    while True:
        try:
            mark = float(input(f"{subject}: "))
            if 0 <= mark <= 100:
                marks.append(mark)
                break
            else:
                print("  Please enter a mark between 0 and 100.\n")
        except ValueError:
            print("  That doesn't look like a number. Try another.\n")

average = sum(marks) / len(marks)

if average >= 90:
    grade, remark = "A", "Outstanding"
elif average >= 75:
    grade, remark = "B", "Keep it up"
elif average >= 60:
    grade, remark = "C", "Not bad"
elif average >= 45:
    grade, remark = "D", "Keep going!"
else:
    grade, remark = "F", "Don't give up"

print("\n--- Your Result ---")
print(f"Average Marks : {average:.1f} / 100")
print(f"Grade         : {grade}")
print(f"Remarks       :  {remark}\n")
