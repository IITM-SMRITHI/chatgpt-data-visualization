"""
Employee Performance Analysis
Email: 23f3004253@ds.study.iitm.ac.in

This script analyzes employee performance data to understand departmental distributions.
It calculates the frequency count for the R&D department and creates a histogram visualization.
"""

import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import base64
from io import BytesIO

# Set style for better-looking plots
sns.set_style("whitegrid")
plt.rcParams['figure.figsize'] = (12, 6)

# Load the employee data
print("=" * 70)
print("Employee Performance Analysis")
print("Email: 23f3004253@ds.study.iitm.ac.in")
print("=" * 70)
print()

df = pd.read_csv('employee_data.csv')

print("Dataset Overview:")
print(f"Total number of employees: {len(df)}")
print(f"Number of departments: {df['department'].nunique()}")
print(f"Departments: {', '.join(sorted(df['department'].unique()))}")
print()

# Calculate the frequency count for the "R&D" department
rd_count = df[df['department'] == 'R&D'].shape[0]
print("=" * 70)
print(f"Frequency count for R&D department: {rd_count}")
print("=" * 70)
print()

# Calculate frequency for all departments
dept_counts = df['department'].value_counts().sort_index()
print("Department-wise Employee Distribution:")
print(dept_counts)
print()

# Create a histogram showing the distribution of departments
fig, ax = plt.subplots(figsize=(12, 7))

# Get department counts and sort them
dept_data = df['department'].value_counts().sort_values(ascending=False)

# Create bar plot
colors = sns.color_palette("husl", len(dept_data))
bars = ax.bar(range(len(dept_data)), dept_data.values, color=colors, edgecolor='black', linewidth=1.2)

# Customize the plot
ax.set_xlabel('Department', fontsize=13, fontweight='bold')
ax.set_ylabel('Number of Employees', fontsize=13, fontweight='bold')
ax.set_title('Employee Distribution Across Departments\nRetail Company Workforce Analysis', 
             fontsize=15, fontweight='bold', pad=20)
ax.set_xticks(range(len(dept_data)))
ax.set_xticklabels(dept_data.index, rotation=45, ha='right', fontsize=11)

# Add value labels on top of bars
for i, (bar, value) in enumerate(zip(bars, dept_data.values)):
    height = bar.get_height()
    ax.text(bar.get_x() + bar.get_width()/2., height,
            f'{int(value)}',
            ha='center', va='bottom', fontsize=10, fontweight='bold')

# Add grid for better readability
ax.yaxis.grid(True, linestyle='--', alpha=0.7)
ax.set_axisbelow(True)

# Highlight R&D department
rd_index = list(dept_data.index).index('R&D')
bars[rd_index].set_color('#FF6B6B')
bars[rd_index].set_edgecolor('darkred')
bars[rd_index].set_linewidth(2)

# Add legend for R&D highlight
from matplotlib.patches import Patch
legend_elements = [Patch(facecolor='#FF6B6B', edgecolor='darkred', label='R&D Department (Highlighted)')]
ax.legend(handles=legend_elements, loc='upper right', fontsize=10)

plt.tight_layout()

# Save the plot
plt.savefig('department_distribution.png', dpi=300, bbox_inches='tight')
print("Visualization saved as 'department_distribution.png'")

# Convert plot to base64 for HTML embedding
buffer = BytesIO()
plt.savefig(buffer, format='png', dpi=300, bbox_inches='tight')
buffer.seek(0)
image_base64 = base64.b64encode(buffer.read()).decode()
buffer.close()

# Prepare data for HTML
total_emp = len(df)
num_depts = df['department'].nunique()
num_regions = df['region'].nunique()
avg_perf = df['performance_score'].mean()
rd_pct = (rd_count/total_emp*100)
rd_avg_perf = df[df['department'] == 'R&D']['performance_score'].mean()
rd_avg_exp = df[df['department'] == 'R&D']['years_experience'].mean()
rd_avg_sat = df[df['department'] == 'R&D']['satisfaction_rating'].mean()
dept_counts_str = dept_counts.to_string()

# Create HTML file with code and visualization
html_content = '''<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Employee Performance Analysis</title>
    <style>
        body {
            font-family: 'Segoe UI', Tahoma, Geneva, Verdana, sans-serif;
            max-width: 1200px;
            margin: 0 auto;
            padding: 20px;
            background-color: #f5f5f5;
            color: #333;
        }
        .header {
            background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
            color: white;
            padding: 30px;
            border-radius: 10px;
            margin-bottom: 30px;
            box-shadow: 0 4px 6px rgba(0,0,0,0.1);
        }
        .header h1 {
            margin: 0 0 10px 0;
            font-size: 2.5em;
        }
        .header p {
            margin: 5px 0;
            font-size: 1.1em;
            opacity: 0.9;
        }
        .section {
            background: white;
            padding: 25px;
            margin-bottom: 25px;
            border-radius: 8px;
            box-shadow: 0 2px 4px rgba(0,0,0,0.1);
        }
        .section h2 {
            color: #667eea;
            border-bottom: 3px solid #667eea;
            padding-bottom: 10px;
            margin-top: 0;
        }
        .result-box {
            background-color: #f0f4ff;
            border-left: 4px solid #667eea;
            padding: 20px;
            margin: 15px 0;
            border-radius: 4px;
        }
        .result-box h3 {
            margin-top: 0;
            color: #667eea;
        }
        .highlight {
            background-color: #fff3cd;
            border-left: 4px solid #ffc107;
            padding: 15px;
            margin: 15px 0;
            border-radius: 4px;
            font-size: 1.3em;
            font-weight: bold;
            color: #856404;
        }
        pre {
            background-color: #f8f9fa;
            border: 1px solid #dee2e6;
            border-radius: 5px;
            padding: 15px;
            overflow-x: auto;
            font-size: 0.9em;
            line-height: 1.5;
        }
        code {
            font-family: 'Courier New', monospace;
            color: #d63384;
        }
        .visualization {
            text-align: center;
            margin: 25px 0;
        }
        .visualization img {
            max-width: 100%;
            height: auto;
            border-radius: 8px;
            box-shadow: 0 4px 8px rgba(0,0,0,0.1);
        }
        .stats-grid {
            display: grid;
            grid-template-columns: repeat(auto-fit, minmax(200px, 1fr));
            gap: 15px;
            margin: 20px 0;
        }
        .stat-card {
            background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
            color: white;
            padding: 20px;
            border-radius: 8px;
            text-align: center;
            box-shadow: 0 2px 4px rgba(0,0,0,0.1);
        }
        .stat-card h4 {
            margin: 0 0 10px 0;
            font-size: 0.9em;
            opacity: 0.9;
            text-transform: uppercase;
            letter-spacing: 1px;
        }
        .stat-card p {
            margin: 0;
            font-size: 2em;
            font-weight: bold;
        }
        .footer {
            text-align: center;
            margin-top: 40px;
            padding: 20px;
            color: #666;
            border-top: 2px solid #dee2e6;
        }
    </style>
</head>
<body>
    <div class="header">
        <h1>📊 Employee Performance Analysis</h1>
        <p><strong>Business Case:</strong> Retail Company Workforce Distribution Analysis</p>
        <p><strong>Contact:</strong> 23f3004253@ds.study.iitm.ac.in</p>
        <p><strong>Date:</strong> November 21, 2025</p>
    </div>

    <div class="section">
        <h2>📋 Executive Summary</h2>
        <p>This analysis examines employee performance data across multiple departments and regions for a Retail company. 
        The goal is to understand departmental distributions, identify patterns, and inform resource allocation decisions 
        for strategic workforce planning.</p>
        
        <div class="stats-grid">
            <div class="stat-card">
                <h4>Total Employees</h4>
                <p>''' + str(total_emp) + '''</p>
            </div>
            <div class="stat-card">
                <h4>Departments</h4>
                <p>''' + str(num_depts) + '''</p>
            </div>
            <div class="stat-card">
                <h4>Regions</h4>
                <p>''' + str(num_regions) + '''</p>
            </div>
            <div class="stat-card">
                <h4>Avg Performance</h4>
                <p>''' + f'{avg_perf:.1f}' + '''</p>
            </div>
        </div>
    </div>

    <div class="section">
        <h2>🎯 Key Finding: R&D Department Analysis</h2>
        <div class="highlight">
            Frequency count for R&D department: ''' + str(rd_count) + ''' employees
        </div>
        <div class="result-box">
            <h3>R&D Department Statistics</h3>
            <ul>
                <li><strong>Total Employees:</strong> ''' + str(rd_count) + '''</li>
                <li><strong>Percentage of Workforce:</strong> ''' + f'{rd_pct:.1f}' + '''%</li>
                <li><strong>Average Performance Score:</strong> ''' + f'{rd_avg_perf:.2f}' + '''</li>
                <li><strong>Average Years Experience:</strong> ''' + f'{rd_avg_exp:.1f}' + ''' years</li>
                <li><strong>Average Satisfaction Rating:</strong> ''' + f'{rd_avg_sat:.2f}' + '''/5.0</li>
            </ul>
        </div>
    </div>

    <div class="section">
        <h2>📊 Department-wise Distribution</h2>
        <div class="result-box">
            <h3>Employee Count by Department</h3>
            <pre>''' + dept_counts_str + '''</pre>
        </div>
    </div>

    <div class="section">
        <h2>📈 Visualization: Department Distribution Histogram</h2>
        <div class="visualization">
            <img src="data:image/png;base64,''' + image_base64 + '''" alt="Department Distribution Histogram">
            <p style="color: #666; margin-top: 10px; font-style: italic;">
                Figure 1: Employee distribution across departments with R&D department highlighted in red
            </p>
        </div>
    </div>

    <div class="section">
        <h2>💻 Python Code</h2>
        <pre><code>"""
Employee Performance Analysis
Email: 23f3004253@ds.study.iitm.ac.in

This script analyzes employee performance data to understand departmental distributions.
It calculates the frequency count for the R&D department and creates a histogram visualization.
"""

import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Load the employee data
df = pd.read_csv('employee_data.csv')

# Calculate the frequency count for the "R&D" department
rd_count = df[df['department'] == 'R&D'].shape[0]
print(f"Frequency count for R&D department: {rd_count}")

# Create a histogram showing the distribution of departments
plt.figure(figsize=(12, 7))
dept_data = df['department'].value_counts().sort_values(ascending=False)
colors = sns.color_palette("husl", len(dept_data))
bars = plt.bar(range(len(dept_data)), dept_data.values, color=colors)

plt.xlabel('Department', fontsize=13, fontweight='bold')
plt.ylabel('Number of Employees', fontsize=13, fontweight='bold')
plt.title('Employee Distribution Across Departments', fontsize=15, fontweight='bold')
plt.xticks(range(len(dept_data)), dept_data.index, rotation=45, ha='right')

# Highlight R&D department
rd_index = list(dept_data.index).index('R&D')
bars[rd_index].set_color('#FF6B6B')

plt.tight_layout()
plt.savefig('department_distribution.png', dpi=300)
plt.show()
</code></pre>
    </div>

    <div class="section">
        <h2>🔍 Insights & Recommendations</h2>
        <div class="result-box">
            <h3>Key Insights:</h3>
            <ul>
                <li>The R&D department comprises ''' + f'{rd_pct:.1f}' + '''% of the total workforce with ''' + str(rd_count) + ''' employees</li>
                <li>R&D shows strong performance metrics with an average score of ''' + f'{rd_avg_perf:.2f}' + '''</li>
                <li>High satisfaction rating of ''' + f'{rd_avg_sat:.2f}' + '''/5.0 indicates good employee engagement</li>
                <li>The department has experienced staff with an average of ''' + f'{rd_avg_exp:.1f}' + ''' years</li>
            </ul>
            
            <h3>Strategic Recommendations:</h3>
            <ul>
                <li>Consider the R&D department as a benchmark for performance standards</li>
                <li>Analyze best practices from R&D for application across other departments</li>
                <li>Maintain strong investment in R&D given high performance and satisfaction metrics</li>
                <li>Use this distribution analysis to inform balanced recruitment strategies</li>
            </ul>
        </div>
    </div>

    <div class="footer">
        <p><strong>Analysis prepared by:</strong> 23f3004253@ds.study.iitm.ac.in</p>
        <p>Employee Performance Analysis | November 21, 2025</p>
        <p>Retail Company | Strategic Workforce Planning</p>
    </div>
</body>
</html>
'''

# Save the HTML file
with open('employee_analysis.html', 'w', encoding='utf-8') as f:
    f.write(html_content)

print()
print("=" * 70)
print("✓ HTML file created successfully: 'employee_analysis.html'")
print("=" * 70)
print()
print("Summary:")
print(f"  • Dataset contains {len(df)} employees across {df['department'].nunique()} departments")
print(f"  • R&D department has {rd_count} employees ({(rd_count/len(df)*100):.1f}% of workforce)")
print(f"  • Visualization saved as PNG and embedded in HTML")
print(f"  • Email verification: 23f3004253@ds.study.iitm.ac.in")
print()
print("Next steps:")
print("  1. Review the HTML file: employee_analysis.html")
print("  2. Push to GitHub repository")
print("  3. Get the raw GitHub URL for submission")
print()
