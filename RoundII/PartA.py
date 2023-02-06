import pandas as pd #dependency
import numpy as np #dependency

df_teacher = pd.DataFrame({
"name": ["Pep Guardiola", "Jurgen Klopp", "Mikel Arteta", "Zinadine Zidane"],
"married": [True, True, False, True],
"school": ["Manchester High School", "Liverpool High School", "Arsenal High", np.nan]
})

df_student = pd.DataFrame({
"teacher": ["Mikel Arteta", "Mikel Arteta", "Pep Guardiola", "Jurgen Klopp", "Jurgen Klopp", "Jurgen Klopp", "Pep Guardiola","Pep Guardiola","Mikel Arteta"],
"name": ["Bukayo Saka", "Gabriel Martinelli", "Jack Grealish", "Roberto Firmino",
"Andrew Robertson", "Darwin Nunez", "Ederson Moraes", "Manuel Akanji", "Thomas Partey"],
"age": [21, 21, 27, 31, 28, 23, 29, 27, 29],
"height": ['2.1m','2.1m', '2.1m', '2.1m', '2.1m', '2.1m', '2.1m', '2.1m', '2.1m']
})

#Make a copy of the df_teacher
new_df_teachers = df_teacher.copy()

#make a copy of the df_student
new_df_students = df_student.copy()

teachers = []

for i, row in new_df_teachers.iterrows():
    teacher = {
        "name": row["name"],
        "married": row["married"],
        "school": row["school"],
        "students": []
    }
    
    students = new_df_students[new_df_students["teacher"] == row["name"]].to_dict("records")
    teacher["students"] = students
    
    teachers.append(teacher)
    result = {
        "teachers": teachers
    }

print(result)

