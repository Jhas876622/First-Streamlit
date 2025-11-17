📊 Advanced Data Visualizer

An interactive Streamlit-based data exploration and visualization tool that lets you upload datasets, view summaries, analyze missing values, and generate a wide range of interactive visualizations — all without writing a single line of code.

🚀 Features
🔹 1. Upload & Load Data Easily

Upload your own CSV dataset

Choose from built-in sample datasets (Iris, Tips, Stock Prices)

Or generate random synthetic data for experimentation

🔹 2. Dataset Overview

Once a dataset is loaded, the app instantly shows:

Total rows and columns

Count of numeric and categorical features

Data preview (top 10 rows)

Statistical summary using .describe()

🔹 3. Missing Value Analysis

View missing value counts per column

Interactive bar chart (Plotly)

Auto-detects if dataset is free of missing values

📊 Interactive Visualizations

The app offers six major categories of plots — fully customizable.

1️⃣ Basic Charts

Line plots

Bar charts (with aggregation: mean, sum, count)

Area charts

Pie / Donut charts

2️⃣ Statistical Plots

Histograms (with adjustable bins)

Box plots (grouped by category if desired)

Distribution plots (histogram + KDE)

3️⃣ Relationship (Relational) Plots

Scatter plots (with color & size encoding)

Correlation heatmap

Multi-variable relationships

4️⃣ Categorical Analysis

Count plots

Grouped bar charts (cross-tab visualizations)

5️⃣ Advanced Plots

Scatter matrix (Pair Plot)

3D scatter plots

Multi-dimensional data exploration

6️⃣ Custom Analysis

Apply filters to:

Categorical columns (multi-select)

Numeric columns (sliders)

Visualize filtered data using:

Histogram

Box plot

Scatter plot

Line chart

🛠️ Tech Stack
Technology	Purpose
Streamlit	UI & interactive components
Plotly	Dynamic visualizations
Seaborn / Matplotlib	Statistical plots
Pandas / NumPy	Data handling & computation
CSS customization	Enhanced UI styling
📥 Installation & Usage
1. Clone the repository
git clone https://github.com/your-username/advanced-data-visualizer.git
cd advanced-data-visualizer

2. Install dependencies
pip install -r requirements.txt

3. Run the Streamlit app
streamlit run "Enhanced Data Visualization Streamlit app.py"

📄 File Structure
📁 project-folder
│── 📄 Enhanced Data Visualization Streamlit app.py
│── 📄 requirements.txt
│── 📄 README.md
│── 📁 assets (optional)

❤️ Acknowledgements

Built with love using Streamlit, Plotly, and Python to make data exploration joyful and accessible.
