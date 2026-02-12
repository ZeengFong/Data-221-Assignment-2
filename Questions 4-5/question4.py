import pandas as pd

students_df = pd.read_csv('student.csv')
high_engagement_students_df = students_df[(students_df['studytime'] >= 3) & (students_df['internet'] == 1) & (students_df['absences'] <= 5)]
high_engagement_students_df.to_csv("high_engagement_student.csv",index=False)
hes_count = len(high_engagement_students_df)
hes_average_grade = high_engagement_students_df['grade'].mean()
print(f"There were {hes_count} students saved.")
print(f"The average grade of a high engagement student is {round(hes_average_grade,2)}")