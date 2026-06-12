import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv("train.csv")

print("Shape:", df.shape)
print("\nColumns:")
print(df.columns.tolist())

print("\nMissing Values:")
print(df.isnull().sum())

print("\nDuplicates:", df.duplicated().sum())
print("\nMissing Values:")
print(df.isnull().sum())

print("\nTotal Missing Values:")
print(df.isnull().sum().sum())

print("\nColumns:")
print(df.columns.tolist())

report = {
    "Total Rows": len(df),
    "Total Columns": len(df.columns),
    "Missing Values": int(df.isnull().sum().sum()),
    "Duplicate Rows": int(df.duplicated().sum())
}

report_df = pd.DataFrame([report])

report_df.to_csv("reports/data_quality_report.csv", index=False)

print("Data Quality Report Generated Successfully!")


df["Attrition"].value_counts().plot(kind="bar")

plt.title("Employee Attrition Distribution")
plt.xlabel("Attrition")
plt.ylabel("Number of Employees")

plt.savefig("images/attrition_distribution.png")
plt.show()
plt.figure(figsize=(8,5))

df["Monthly Income"].hist(bins=20)

plt.title("Monthly Income Distribution")
plt.xlabel("Monthly Income")
plt.ylabel("Employees")

plt.savefig("images/salary_distribution.png")
plt.show()
plt.figure(figsize=(6,4))

df["Gender"].value_counts().plot(kind="bar")

plt.title("Gender Distribution")
plt.xlabel("Gender")
plt.ylabel("Count")

plt.savefig("images/gender_distribution.png")
plt.show()
plt.figure(figsize=(10,5))

df["Job Role"].value_counts().head(10).plot(kind="bar")

plt.title("Top Job Roles")
plt.xlabel("Job Role")
plt.ylabel("Employees")

plt.savefig("images/job_role_distribution.png")
plt.show()