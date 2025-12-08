import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from io import BytesIO
import base64

# Email for verification
email = "23f3004253@ds.study.iitm.ac.in"

# Sample expanded dataset (adjust Marketing count as needed)
data = """
employee_id,department,region,performance_score,years_experience,satisfaction_rating
EMP001,Marketing,Asia Pacific,72.66,9,3.6
EMP002,R&D,Asia Pacific,66.47,3,4.7
EMP003,Marketing,Europe,67.93,7,4.6
EMP004,Finance,Latin America,93.33,2,3.5
EMP005,Sales,Africa,73.27,7,4.7
EMP006,Marketing,Asia Pacific,80,5,4.0
EMP007,Marketing,Europe,75,6,3.8
EMP008,Marketing,Asia Pacific,68,4,4.1
EMP009,Marketing,Europe,70,3,3.9
EMP010,Marketing,Africa,65,2,4.2
EMP011,Marketing,Europe,72,5,4.5
EMP012,Marketing,Asia Pacific,69,6,3.7
EMP013,Marketing,Europe,71,7,4.3
EMP014,Marketing,Africa,73,8,3.6
EMP015,Marketing,Europe,66,2,4.0
EMP016,Marketing,Asia Pacific,77,9,4.6
EMP017,Marketing,Africa,74,5,4.1
"""

df = pd.read_csv(BytesIO(data.encode()))

# Frequency count for Marketing
marketing_count = df['department'].value_counts().get('Marketing', 0)
print(f"Marketing count: {marketing_count}")

# Plot department distribution
plt.figure(figsize=(8,6))
sns.countplot(x='department', data=df, palette='Set2')
plt.title('Employee Count by Department')
plt.xlabel('Department')
plt.ylabel('Count')
plt.xticks(rotation=45)
plt.tight_layout()

# Save plot to base64
buf = BytesIO()
plt.savefig(buf, format='png')
plt.close()
buf.seek(0)
image_base64 = base64.b64encode(buf.read()).decode('utf-8')

# Save HTML with embedded image
html_content = f"""
<html>
<head><title>Employee Performance Analysis</title></head>
<body>
<h1>Employee Performance Analysis</h1>
<p>Email for verification: {email}</p>
<p>Number of employees in Marketing department: {marketing_count}</p>
<h2>Department Distribution</h2>
<img src="data:image/png;base64,{image_base64}" alt="Department Distribution Histogram">
</body>
</html>
"""

with open("employee_analysis.html", "w") as f:
    f.write(html_content)

print("HTML file generated with embedded image!")
