import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# -----------------------------------------
#  Employee Performance Analysis
#  Email: 22f3001098@ds.study.iitm.ac.in
# -----------------------------------------

# Sample dataset (you may replace with full dataset)
data = {
    "employee_id": ["EMP001","EMP002","EMP003","EMP004","EMP005"],
    "department": ["Operations","Operations","R&D","Sales","Marketing"],
    "region": ["Asia Pacific","North America","Middle East","Africa","Latin America"],
    "performance_score": [83.27,84.03,70.68,60.87,78.6],
    "years_experience": [8,11,10,1,8],
    "satisfaction_rating": [3,3.7,3.8,4.7,3.2]
}

df = pd.DataFrame(data)

# ------------------------------
# Calculate frequency of Marketing
# ------------------------------
marketing_count = (df["department"] == "Marketing").sum()
print("Frequency count for Marketing department:", marketing_count)

# ------------------------------
# Create Histogram of Departments
# ------------------------------
plt.figure(figsize=(8, 5))
sns.countplot(x=df["department"])
plt.title("Department Distribution")
plt.xlabel("Department")
plt.ylabel("Count")
plt.tight_layout()

# Save plot
plt.savefig("department_histogram.png")

# ------------------------------
# Save everything into an HTML file
# ------------------------------
html_content = f"""
<html>
<head>
    <title>Employee Performance Analysis</title>
</head>
<body>
<h1>Employee Performance Analysis</h1>
<p><b>Email:</b> 22f3001098@ds.study.iitm.ac.in</p>
<p><b>Marketing Department Frequency Count:</b> {marketing_count}</p>
<img src="department_histogram.png" width="500">
</body>
</html>
"""

with open("employee_analysis.html", "w") as f:
    f.write(html_content)

print("HTML file generated: employee_analysis.html")
employee_analysis.py
