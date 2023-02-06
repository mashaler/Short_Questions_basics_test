import pandas as pd

df_teacher = pd.DataFrame({
    "name": ["Pep Guardiola", "Jurgen Klopp", "Mikel Arteta", "Zinedine Zidane"], 
    "school": ["Manchester High School", "Liverpool High School", "Arsenal High", None], 
    "married": [True, True, False, True]
})

df_student = pd.DataFrame({
    "teacher": ["Mikel Arteta", "Mikel Arteta", "Pep Guardiola", "Jurgen Klopp", "Jurgen Klopp", "Jurgen Klopp", "Pep Guardiola","Pep Guardiola","Mikel Arteta"], 
   "student": ["Bukayo Saka", "Gabriel Martinelli", "Jack Grealish", "Roberto Firmino", "Andrew Robertson", "Darwin Nunez", "Ederson Moraes", "Manuel Akanji", "ThomasPartey"],
    "age": [21, 21, 27, 31, 28, 23, 29, 27, 29], 
    "height": ['2.1m','2.1m', '2.1m', '2.1m', '2.1m', '2.1m', '2.1m', '2.1m','2.1m'],
    "weight": ['80kg','70kg','690kg','73kg','60kg','70kg','80kg','88kg','74kg',]


})

#Make a copy of the df_teacher
new_df_teachers = df_teacher.copy()

#make a copy of the df_student
new_df_students = df_student.copy()


result = {
    "teachers": []
}

for index, row in new_df_teachers.iterrows():
    teacher = {
        "teacher": row["name"], 
        "school": row["school"], 
        "married": row["married"], 
        "students": []
    }
    
    students = new_df_students[new_df_students["teacher"] == row["name"]]
    students_list = students.to_dict("records")
    
    for student in students_list:
        teacher["students"].append({
            "student": student["student"], 
            "age": student["age"], 
            "height": student["height"],
            "weight": student["weight"]

        })
    
    result["teachers"].append(teacher)

print(result)
