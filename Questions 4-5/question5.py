import pandas as pd

student_df = pd.read_csv('student.csv')
student_df['grade_band'] = student_df['grade'].apply(lambda x: "Low" if x <= 9 else ("Medium" if x <= 14 else "High"))

student_summary_table = student_df.groupby('grade_band').agg(
    student_count=('grade', 'count'),
    avg_absences=('absences', 'mean'),
    pct_internet=('internet', 'mean')
)

student_summary_table.to_csv('student_bands.csv')

print(student_summary_table)