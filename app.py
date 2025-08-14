import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import streamlit as st

# 🔷 Sidebar Navigation
st.sidebar.title("🔍 Navigation")
section = st.sidebar.radio("Go to section:", [
    "📊 Dashboard Overview", 
    "🔌 Integration Plan", 
    "🛠 Prototype Tools", 
    "🔁 Change Management"
])

# 🧠 Streamlit Dashboard Sections
st.title("🧠 Intelligent Demand Forecasting System")

# 📊 Main Dashboard (default view)
if section == "📊 Dashboard Overview":
    st.markdown("### Welcome to the Forecasting & Reorder Dashboard")
    st.write("Use the sidebar to explore how our prototype integrates and supports decision-making.")

# 🔌 Integration Plan
elif section == "🔌 Integration Plan":
    st.markdown("## 🔌 Integration Plan")
    st.image("integration_diagram.png", caption="System Integration Workflow", use_column_width=True)
    st.markdown("""
    - Integrated with Inventory Management System (CSV/API)
    - Forecasting Engine built using Prophet & Classical ML
    - Outputs plugged into ERP or Reorder systems
    """)

# 🛠 Prototype Tools
elif section == "🛠 Prototype Tools":
    st.markdown("## 🛠 Prototype Tools")
    st.markdown("""
    - **Working Forecasting Model**: Supports daily/monthly predictions using Prophet and ML
    - **Visual Interface**: Charts, metrics, and recommendations
    - **Reorder Generator**: Auto-calculates reorder points
    """)
    st.success("Prototype built with Python + Streamlit")

# 🔁 Change Management
elif section == "🔁 Change Management":
    st.markdown("## 🔁 Change Management")
    st.markdown("""
    - **Transparency**: Forecast logic and inputs shown clearly
    - **Ease of Use**: Clean UI for non-technical users
    - **Adoption Support**: Minimizes resistance by aligning with current Excel workflows
    """)
    st.info("This dashboard reduces adoption barriers across planning teams.")



# -----------------------
# LOAD DATA
# -----------------------
df_forecast = pd.read_csv("prophet_forecast.csv")
df_reorder = pd.read_csv("reorder_plan_all_products.csv")
df_actual = pd.read_csv("engineered_dataset.csv")

# Convert 'ds' to datetime
df_forecast['ds'] = pd.to_datetime(df_forecast['ds'])
df_reorder['ds'] = pd.to_datetime(df_reorder['ds'])
df_actual['ds'] = pd.to_datetime(df_actual['ds'])

# -----------------------
# SIDEBAR - PRODUCT SELECTION
# -----------------------
st.sidebar.title(" Filter")
product_list = df_reorder['product_name'].unique()
selected_product = st.sidebar.selectbox("Select a product", product_list)

# Filter data for the selected product
product_forecast = df_reorder[df_reorder['product_name'] == selected_product]
product_actual = df_actual[df_actual['product_name'] == selected_product]

# -----------------------
# TITLE + METRICS
# -----------------------
st.title(" Demand Forecasting & Reorder Dashboard")
st.subheader(f"Product: **{selected_product}**")

latest_inventory = product_forecast['current_inventory'].iloc[0]
next_reorder_day = product_forecast[product_forecast['reorder_flag'] == True]['ds'].min()

st.metric(" Current Inventory", f"{latest_inventory}")
st.metric(" Next Reorder Needed", f"{next_reorder_day.date() if pd.notnull(next_reorder_day) else 'Not Needed'}")

# -----------------------
# CHART 1: Forecasted Demand vs Actual
# -----------------------
st.markdown("###  Prophet Forecast vs Actual Demand")

df_plot = pd.merge(
    product_forecast[['ds', 'forecasted_demand']],
    product_actual.groupby('ds').agg({'y': 'sum'}).reset_index(),
    on='ds',
    how='left'
)

fig1, ax1 = plt.subplots(figsize=(10, 4))
ax1.plot(df_plot['ds'], df_plot['forecasted_demand'], label='Forecast', color='orange')
ax1.plot(df_plot['ds'], df_plot['y'], label='Actual', color='green')
ax1.set_title("Forecasted vs Actual Demand")
ax1.legend()
st.pyplot(fig1)

# -----------------------
# CHART 2: Reorder Quantity Over Time
# -----------------------
st.markdown("###  Reorder Alerts & Quantities")

fig2, ax2 = plt.subplots(figsize=(10, 4))
ax2.bar(product_forecast['ds'], product_forecast['reorder_quantity'], color='red')
ax2.set_title("Reorder Quantities Over Time")
ax2.set_ylabel("Units to Reorder")
st.pyplot(fig2)

# -----------------------
# Table Preview
# -----------------------
with st.expander(" View Reorder Plan Table"):
    st.dataframe(product_forecast[['ds', 'forecasted_demand', 'current_inventory', 'reorder_flag', 'reorder_quantity']])

st.download_button("Download Reorder Plan CSV", product_forecast.to_csv(index=False), file_name="reorder_plan.csv")
