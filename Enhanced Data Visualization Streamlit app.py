import numpy as np
import pandas as pd
import streamlit as st
import seaborn as sns
import matplotlib.pyplot as plt
import plotly.express as px
import plotly.graph_objects as go
import plotly.figure_factory as ff
from plotly.subplots import make_subplots
import warnings
warnings.filterwarnings('ignore')

# Page configuration
st.set_page_config(
    page_title="📊 Advanced Data Visualizer",
    page_icon="📊",
    layout="wide",
    initial_sidebar_state="expanded"
)

# Custom CSS for better styling
st.markdown("""
<style>
    .main-header {
        font-size: 3rem;
        color: #1f77b4;
        text-align: center;
        margin-bottom: 2rem;
        background: linear-gradient(90deg, #1f77b4, #ff7f0e);
        -webkit-background-clip: text;
        -webkit-text-fill-color: transparent;
        font-weight: bold;
    }
    .section-header {
        font-size: 1.5rem;
        color: #2e4057;
        margin-top: 2rem;
        margin-bottom: 1rem;
        border-left: 5px solid #1f77b4;
        padding-left: 10px;
    }
    .metric-container {
        background-color: #f0f2f6;
        padding: 1rem;
        border-radius: 10px;
        margin: 0.5rem 0;
    }
    .stTabs [data-baseweb="tab-list"] {
        gap: 2px;
    }
    .stTabs [data-baseweb="tab"] {
        height: 50px;
        padding-left: 20px;
        padding-right: 20px;
    }
</style>
""", unsafe_allow_html=True)

# Main title
st.markdown('<h1 class="main-header">📊 Advanced Data Visualizer</h1>', unsafe_allow_html=True)

# Sidebar for navigation and controls
with st.sidebar:
    st.markdown("## 🎛️ Control Panel")

    # Data source selection
    data_source = st.selectbox(
        "📁 Choose Data Source",
        ["Upload Dataset", "Sample Datasets", "Generate Random Data"]
    )

    # Color theme selection
    color_theme = st.selectbox(
        "🎨 Color Theme",
        ["Default", "Viridis", "Plasma", "Set1", "Dark2", "Pastel1"]
    )

# Initialize session state for data
if 'df' not in st.session_state:
    st.session_state.df = None

# Data loading section
def load_sample_data(dataset_name):
    """Load sample datasets"""
    if dataset_name == "Iris":
        # Create sample iris data since we don't have the file
        np.random.seed(42)
        iris_data = {
            'sepal_length': np.random.normal(5.8, 0.8, 150),
            'sepal_width': np.random.normal(3.0, 0.4, 150),
            'petal_length': np.random.normal(3.8, 1.8, 150),
            'petal_width': np.random.normal(1.2, 0.8, 150),
            'species': np.random.choice(['setosa', 'versicolor', 'virginica'], 150)
        }
        return pd.DataFrame(iris_data)
    elif dataset_name == "Tips":
        # Create sample tips data
        np.random.seed(42)
        tips_data = {
            'total_bill': np.random.normal(20, 8, 244),
            'tip': np.random.normal(3, 1.5, 244),
            'sex': np.random.choice(['Male', 'Female'], 244),
            'smoker': np.random.choice(['Yes', 'No'], 244),
            'day': np.random.choice(['Thur', 'Fri', 'Sat', 'Sun'], 244),
            'time': np.random.choice(['Lunch', 'Dinner'], 244),
            'size': np.random.choice([1, 2, 3, 4, 5, 6], 244)
        }
        return pd.DataFrame(tips_data)
    elif dataset_name == "Stock Prices":
        # Create sample stock data
        dates = pd.date_range('2023-01-01', periods=100, freq='D')
        np.random.seed(42)
        price = 100
        prices = []
        for _ in range(100):
            price += np.random.normal(0, 2)
            prices.append(max(price, 10))  # Ensure positive prices
        return pd.DataFrame({'Date': dates, 'Price': prices, 'Volume': np.random.randint(1000, 10000, 100)})

# Data loading logic
if data_source == "Upload Dataset":
    st.markdown('<div class="section-header">📤 Upload Your Dataset</div>', unsafe_allow_html=True)
    uploaded_file = st.file_uploader(
        "Choose a CSV file",
        type=['csv'],
        help="Upload a CSV file to visualize your data"
    )

    if uploaded_file is not None:
        try:
            df = pd.read_csv(uploaded_file)
            st.session_state.df = df
            st.success(f"✅ Successfully loaded dataset with {df.shape[0]} rows and {df.shape[1]} columns!")
        except Exception as e:
            st.error(f"❌ Error loading file: {str(e)}")

elif data_source == "Sample Datasets":
    st.markdown('<div class="section-header">📚 Sample Datasets</div>', unsafe_allow_html=True)
    sample_dataset = st.selectbox(
        "Choose a sample dataset",
        ["Iris", "Tips", "Stock Prices"]
    )

    if st.button("Load Sample Dataset"):
        df = load_sample_data(sample_dataset)
        st.session_state.df = df
        st.success(f"✅ Loaded {sample_dataset} dataset!")

elif data_source == "Generate Random Data":
    st.markdown('<div class="section-header">🎲 Generate Random Data</div>', unsafe_allow_html=True)

    col1, col2 = st.columns(2)
    with col1:
        n_rows = st.number_input("Number of rows", min_value=10, max_value=1000, value=100)
    with col2:
        n_cols = st.number_input("Number of columns", min_value=2, max_value=10, value=4)

    if st.button("Generate Random Dataset"):
        np.random.seed(42)
        data = {}
        for i in range(n_cols):
            if i == 0:
                data[f'Category'] = np.random.choice(['A', 'B', 'C', 'D'], n_rows)
            else:
                data[f'Feature_{i}'] = np.random.randn(n_rows)

        df = pd.DataFrame(data)
        st.session_state.df = df
        st.success(f"✅ Generated random dataset with {n_rows} rows and {n_cols} columns!")

# Main visualization section
if st.session_state.df is not None:
    df = st.session_state.df

    # Dataset overview
    st.markdown('<div class="section-header">📋 Dataset Overview</div>', unsafe_allow_html=True)

    col1, col2, col3, col4 = st.columns(4)
    with col1:
        st.metric("📊 Rows", df.shape[0])
    with col2:
        st.metric("📈 Columns", df.shape[1])
    with col3:
        st.metric("🔢 Numeric Columns", len(df.select_dtypes(include=[np.number]).columns))
    with col4:
        st.metric("🔤 Categorical Columns", len(df.select_dtypes(include=['object', 'category']).columns))

    # Data preview
    with st.expander("👀 Data Preview", expanded=False):
        st.dataframe(df.head(10), use_container_width=True)

    # Statistical summary
    with st.expander("📊 Statistical Summary", expanded=False):
        st.dataframe(df.describe(), use_container_width=True)

    # Missing values
    with st.expander("❓ Missing Values Analysis", expanded=False):
        missing_data = df.isnull().sum()
        if missing_data.sum() > 0:
            fig = px.bar(x=missing_data.index, y=missing_data.values,
                        title="Missing Values by Column",
                        labels={'x': 'Columns', 'y': 'Missing Count'})
            st.plotly_chart(fig, use_container_width=True)
        else:
            st.success("✅ No missing values found in the dataset!")

    # Visualization tabs
    st.markdown('<div class="section-header">📊 Interactive Visualizations</div>', unsafe_allow_html=True)

    # Get numeric and categorical columns
    numeric_cols = df.select_dtypes(include=[np.number]).columns.tolist()
    categorical_cols = df.select_dtypes(include=['object', 'category']).columns.tolist()

    # Create tabs for different visualization types
    tab1, tab2, tab3, tab4, tab5, tab6 = st.tabs([
        "📈 Basic Charts", "📊 Statistical Plots", "🔗 Relationship Plots",
        "📋 Categorical Analysis", "🌐 Advanced Plots", "🎯 Custom Analysis"
    ])

    with tab1:
        st.subheader("Basic Charts")

        if numeric_cols:
            col1, col2 = st.columns(2)

            with col1:
                # Line chart
                st.markdown("**📈 Line Chart**")
                if len(numeric_cols) >= 1:
                    selected_cols = st.multiselect("Select columns for line chart", numeric_cols, default=numeric_cols[:3])
                    if selected_cols:
                        fig = px.line(df, y=selected_cols, title="Line Chart")
                        st.plotly_chart(fig, use_container_width=True)

            with col2:
                # Bar chart
                st.markdown("**📊 Bar Chart**")
                if categorical_cols and numeric_cols:
                    cat_col = st.selectbox("Select categorical column", categorical_cols, key="bar_cat")
                    num_col = st.selectbox("Select numeric column", numeric_cols, key="bar_num")

                    agg_func = st.selectbox("Aggregation function", ["mean", "sum", "count"], key="bar_agg")

                    if agg_func == "count":
                        chart_data = df[cat_col].value_counts()
                    else:
                        chart_data = df.groupby(cat_col)[num_col].agg(agg_func)

                    fig = px.bar(x=chart_data.index, y=chart_data.values,
                               title=f"Bar Chart - {agg_func.title()} of {num_col} by {cat_col}")
                    st.plotly_chart(fig, use_container_width=True)

        # Area chart and pie chart
        col1, col2 = st.columns(2)
        with col1:
            if numeric_cols:
                st.markdown("**📈 Area Chart**")
                area_cols = st.multiselect("Select columns for area chart", numeric_cols, default=numeric_cols[:2], key="area")
                if area_cols:
                    fig = go.Figure()
                    for col in area_cols:
                        fig.add_trace(go.Scatter(y=df[col], fill='tonexty', name=col))
                    fig.update_layout(title="Area Chart")
                    st.plotly_chart(fig, use_container_width=True)

        with col2:
            if categorical_cols:
                st.markdown("**🥧 Pie Chart**")
                pie_col = st.selectbox("Select categorical column for pie chart", categorical_cols, key="pie")
                show_hole = st.checkbox("Donut chart", key="donut")

                pie_data = df[pie_col].value_counts()
                fig = px.pie(values=pie_data.values, names=pie_data.index,
                           title=f"Distribution of {pie_col}",
                           hole=0.4 if show_hole else 0)
                st.plotly_chart(fig, use_container_width=True)

    with tab2:
        st.subheader("Statistical Plots")

        if numeric_cols:
            col1, col2 = st.columns(2)

            with col1:
                # Histogram
                st.markdown("**📊 Histogram**")
                hist_col = st.selectbox("Select column for histogram", numeric_cols, key="hist")
                bins = st.slider("Number of bins", min_value=10, max_value=50, value=20, key="hist_bins")

                fig = px.histogram(df, x=hist_col, nbins=bins, title=f"Histogram of {hist_col}")
                st.plotly_chart(fig, use_container_width=True)

            with col2:
                # Box plot
                st.markdown("**📦 Box Plot**")
                box_col = st.selectbox("Select numeric column", numeric_cols, key="box_num")
                box_cat = st.selectbox("Select categorical column (optional)",
                                     ["None"] + categorical_cols, key="box_cat")

                if box_cat == "None":
                    fig = px.box(df, y=box_col, title=f"Box Plot of {box_col}")
                else:
                    fig = px.box(df, x=box_cat, y=box_col, title=f"Box Plot of {box_col} by {box_cat}")
                st.plotly_chart(fig, use_container_width=True)

            # Distribution plot
            st.markdown("**📈 Distribution Plot**")
            dist_col = st.selectbox("Select column for distribution", numeric_cols, key="dist")

            col1, col2 = st.columns(2)
            with col1:
                show_hist = st.checkbox("Show histogram", value=True, key="dist_hist")
            with col2:
                show_kde = st.checkbox("Show KDE", value=True, key="dist_kde")

            fig = ff.create_distplot([df[dist_col].dropna()], [dist_col],
                                   show_hist=show_hist, show_rug=False)
            st.plotly_chart(fig, use_container_width=True)

    with tab3:
        st.subheader("Relationship Plots")

        if len(numeric_cols) >= 2:
            # Scatter plot
            st.markdown("**⚡ Scatter Plot**")
            col1, col2, col3 = st.columns(3)

            with col1:
                x_col = st.selectbox("X-axis", numeric_cols, key="scatter_x")
            with col2:
                y_col = st.selectbox("Y-axis", numeric_cols, key="scatter_y", index=1 if len(numeric_cols) > 1 else 0)
            with col3:
                color_col = st.selectbox("Color by", ["None"] + categorical_cols, key="scatter_color")

            size_col = st.selectbox("Size by (optional)", ["None"] + numeric_cols, key="scatter_size")

            fig = px.scatter(df, x=x_col, y=y_col,
                           color=color_col if color_col != "None" else None,
                           size=size_col if size_col != "None" else None,
                           title=f"Scatter Plot: {x_col} vs {y_col}")
            st.plotly_chart(fig, use_container_width=True)

            # Correlation heatmap
            st.markdown("**🔥 Correlation Heatmap**")
            correlation_matrix = df[numeric_cols].corr()

            fig = px.imshow(correlation_matrix,
                          title="Correlation Heatmap",
                          color_continuous_scale="RdBu",
                          aspect="auto")
            fig.update_layout(width=800, height=600)
            st.plotly_chart(fig, use_container_width=True)

    with tab4:
        st.subheader("Categorical Analysis")

        if categorical_cols:
            # Count plot
            st.markdown("**📊 Count Plot**")
            count_col = st.selectbox("Select categorical column", categorical_cols, key="count")

            count_data = df[count_col].value_counts()
            fig = px.bar(x=count_data.index, y=count_data.values,
                       title=f"Count Plot of {count_col}")
            st.plotly_chart(fig, use_container_width=True)

            if len(categorical_cols) >= 2:
                # Grouped bar chart
                st.markdown("**📊 Grouped Analysis**")
                col1, col2 = st.columns(2)

                with col1:
                    group_col1 = st.selectbox("Primary grouping", categorical_cols, key="group1")
                with col2:
                    group_col2 = st.selectbox("Secondary grouping", categorical_cols, key="group2")

                if group_col1 != group_col2:
                    crosstab = pd.crosstab(df[group_col1], df[group_col2])
                    fig = px.bar(crosstab, title=f"Cross-tabulation: {group_col1} vs {group_col2}")
                    st.plotly_chart(fig, use_container_width=True)

    with tab5:
        st.subheader("Advanced Plots")

        if numeric_cols and len(numeric_cols) >= 2:
            # Pair plot (simplified)
            st.markdown("**🔗 Pair Plot Matrix**")
            selected_numeric = st.multiselect("Select columns for pair plot",
                                            numeric_cols,
                                            default=numeric_cols[:3],
                                            key="pair")

            if len(selected_numeric) >= 2:
                fig = px.scatter_matrix(df[selected_numeric], title="Pair Plot Matrix")
                fig.update_layout(height=800)
                st.plotly_chart(fig, use_container_width=True)

            # 3D Scatter plot
            if len(numeric_cols) >= 3:
                st.markdown("**🌐 3D Scatter Plot**")
                col1, col2, col3 = st.columns(3)

                with col1:
                    x3d = st.selectbox("X-axis", numeric_cols, key="3d_x")
                with col2:
                    y3d = st.selectbox("Y-axis", numeric_cols, key="3d_y", index=1)
                with col3:
                    z3d = st.selectbox("Z-axis", numeric_cols, key="3d_z", index=2)

                color3d = st.selectbox("Color by", ["None"] + categorical_cols, key="3d_color")

                fig = px.scatter_3d(df, x=x3d, y=y3d, z=z3d,
                                  color=color3d if color3d != "None" else None,
                                  title="3D Scatter Plot")
                st.plotly_chart(fig, use_container_width=True)

    with tab6:
        st.subheader("Custom Analysis")

        # Data filtering
        st.markdown("**🔍 Data Filtering**")

        filtered_df = df.copy()

        # Add filters for categorical columns
        for col in categorical_cols:
            unique_values = df[col].unique()
            selected_values = st.multiselect(f"Filter {col}",
                                           unique_values,
                                           default=unique_values,
                                           key=f"filter_{col}")
            if selected_values:
                filtered_df = filtered_df[filtered_df[col].isin(selected_values)]

        # Add filters for numeric columns
        for col in numeric_cols:
            col_min, col_max = float(df[col].min()), float(df[col].max())
            selected_range = st.slider(f"Range for {col}",
                                     col_min, col_max,
                                     (col_min, col_max),
                                     key=f"range_{col}")
            filtered_df = filtered_df[(filtered_df[col] >= selected_range[0]) &
                                    (filtered_df[col] <= selected_range[1])]

        st.info(f"Filtered dataset: {filtered_df.shape[0]} rows (from {df.shape[0]} original rows)")

        # Show filtered data
        if st.checkbox("Show filtered data"):
            st.dataframe(filtered_df, use_container_width=True)

        # Custom visualization on filtered data
        if not filtered_df.empty and numeric_cols:
            st.markdown("**📊 Custom Visualization on Filtered Data**")

            chart_type = st.selectbox("Select chart type",
                                    ["Histogram", "Box Plot", "Scatter Plot", "Line Chart"])

            if chart_type == "Histogram" and numeric_cols:
                hist_col = st.selectbox("Select column", numeric_cols, key="custom_hist")
                fig = px.histogram(filtered_df, x=hist_col, title=f"Filtered Histogram of {hist_col}")
                st.plotly_chart(fig, use_container_width=True)

            elif chart_type == "Box Plot" and numeric_cols:
                box_col = st.selectbox("Select column", numeric_cols, key="custom_box")
                fig = px.box(filtered_df, y=box_col, title=f"Filtered Box Plot of {box_col}")
                st.plotly_chart(fig, use_container_width=True)

            elif chart_type == "Scatter Plot" and len(numeric_cols) >= 2:
                col1, col2 = st.columns(2)
                with col1:
                    x_col = st.selectbox("X-axis", numeric_cols, key="custom_scatter_x")
                with col2:
                    y_col = st.selectbox("Y-axis", numeric_cols, key="custom_scatter_y",
                                       index=1 if len(numeric_cols) > 1 else 0)

                fig = px.scatter(filtered_df, x=x_col, y=y_col,
                               title=f"Filtered Scatter Plot: {x_col} vs {y_col}")
                st.plotly_chart(fig, use_container_width=True)

            elif chart_type == "Line Chart" and numeric_cols:
                line_cols = st.multiselect("Select columns", numeric_cols, key="custom_line")
                if line_cols:
                    fig = px.line(filtered_df, y=line_cols, title="Filtered Line Chart")
                    st.plotly_chart(fig, use_container_width=True)

else:
    # Welcome message when no data is loaded
    st.markdown("""
    <div style="text-align: center; padding: 50px;">
        <h2>🚀 Welcome to Advanced Data Visualizer!</h2>
        <p style="font-size: 1.2em; color: #666;">
            Get started by selecting a data source from the sidebar:
        </p>
        <ul style="text-align: left; display: inline-block; font-size: 1.1em;">
            <li>📤 <strong>Upload Dataset:</strong> Upload your own CSV file</li>
            <li>📚 <strong>Sample Datasets:</strong> Explore with pre-loaded datasets</li>
            <li>🎲 <strong>Generate Random Data:</strong> Create synthetic data for testing</li>
        </ul>
        <p style="font-size: 1.1em; color: #666; margin-top: 30px;">
            Once loaded, you'll have access to interactive visualizations, statistical analysis, and advanced plotting features!
        </p>
    </div>
    """, unsafe_allow_html=True)

# Footer
st.markdown("---")
st.markdown(
    """
    <div style="text-align: center; color: #666; padding: 20px;">
        📊 Advanced Data Visualizer | Built with ❤️ using Streamlit & Plotly
    </div>
    """,
    unsafe_allow_html=True
)
