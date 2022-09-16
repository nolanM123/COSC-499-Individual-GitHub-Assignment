import sort
import search

class_grades: list[tuple[str, int]] = [
    ("Nolan M.", 83),
    ("James T.", 56),
    ("Lisa S.", 99),
    ("Grace P.", 73),
    ("Todd F.", 65),
]

if __name__ == "__main__":
    sort.quick_sort(class_grades, lambda studentinfo: studentinfo[1])

    print("Ranked grades: ")
    for rank, (student, grade) in enumerate(class_grades, 1):
        print(f"({rank}) {student}")
    
    while True:
        student: str = input("Find grade (Enter student name): ")
        i: int = search.linear_search(class_grades, student, lambda studentinfo: studentinfo[0])

        if i != -1:
            grade: int = class_grades[i][1]
            print(f"{student}, Achived an overall grade of {grade}.")
            break
