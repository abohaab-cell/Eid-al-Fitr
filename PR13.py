name = "hamada codezilla"
grades = {
"math": 99,
"english": 98,
"science": 99,
"arabic": 100,
"history": 99
}

def clicing_name_1(names):
    i = 0
    for j in names:

        if j != " ":
            i += 1
        else:
            break
    return names[:i+1]
def clicing_name_2(names):
    return names[len(clicing_name_1(names)):]

def print_student(name,grades):
    print(f"Student: {clicing_name_1(name)}")
    print(f"School: {clicing_name_2(name)}")
    print(8*'-')
    for i in grades:
        print(f"{i}: {grades[i]}")


print_student(name, grades)