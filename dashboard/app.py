import streamlit as st
import pandas as pd
import plotly.express as px
import plotly.graph_objects as go
import os

# ==========================================
# 1. PAGE CONFIGURATION
# ==========================================
st.set_page_config(
    page_title="Ethiopia Financial Inclusion Forecast",
    page_icon="🇪🇹",
    layout="wide",
    initial_sidebar_state="expanded"
)

# Custom CSS for styling
st.markdown("""
<style>
    .main-metric {font-size: 32px; font-weight: bold; color: #2c3e50;}
    .sub-metric {font-size: 14px; color: #7f8c8d;}
    .stAlert {margin-top: 20px;}
</style>
""", unsafe_allow_html=True)

# ==========================================
# 2. DATA LOADING
# ==========================================
@st.cache_data
def load_data():
    # Define paths (Assumes running from project root)
    hist_path = 'data/processed/ethiopia_fi_enriched.csv'
    fc_path = 'data/processed/forecast_results.csv'
    
    # Check if files exist
    if not os.path.exists(hist_path) or not os.path.exists(fc_path):
        return None, None

    # Load History
    df_hist = pd.read_csv(hist_path, parse_dates=['observation_date'])
    df_hist = df_hist[df_hist['record_type'] == 'observation']
    
    # Load Forecast
    df_fc = pd.read_csv(fc_path)
    
    return df_hist, df_fc

hist_df, fc_df = load_data()

# Error Handling
if hist_df is None:
    st.error("❌ Data missing! Please run the Notebooks (Task 1-4) to generate the CSV files in `data/processed/`.")
    st.stop()

# ==========================================
# 3. SIDEBAR NAVIGATION
# ==========================================
st.sidebar.image("https://upload.wikimedia.org/wikipedia/commons/7/71/Flag_of_Ethiopia.svg", width=100)
st.sidebar.title("Selam Analytics")
st.sidebar.markdown("**Project:** Financial Inclusion 2027")

menu = st.sidebar.radio(
    "Navigation", 
    ["📊 Executive Overview", "📉 Trend Analysis", "🔮 Forecast Engine", "📋 Policy Insights"]
)

st.sidebar.markdown("---")
st.sidebar.info(
    """
    **Data Sources:**
    - Global Findex (World Bank)
    - EthioTelecom Reports
    - NBE Directives
    """
)

# ==========================================
# 4. PAGE: EXECUTIVE OVERVIEW
# ==========================================
if menu == "📊 Executive Overview":
    st.title("🇪🇹 Financial Inclusion Outlook (2025-2027)")
    st.markdown("Tracking Ethiopia's progress toward the **National Financial Inclusion Strategy (NFIS)** goals.")

    # Key Metrics (Most recent actuals)
    last_acc = hist_df[hist_df['indicator_code']=='ACC_OWNERSHIP']['value_numeric'].max()
    last_mm = hist_df[hist_df['indicator_code']=='ACC_MM_ACCOUNT']['value_numeric'].max()
    telebirr_users = hist_df[hist_df['indicator_code']=='USG_TELEBIRR_USERS']['value_numeric'].max()
    
    # Forecasted 2027 Value (Base Case)
    fc_acc_27 = fc_df[(fc_df['indicator']=='ACC_OWNERSHIP') & (fc_df['year']==2027)]['value'].values[0]

    # KPI Row
    col1, col2, col3, col4 = st.columns(4)
    with col1:
        st.metric("Account Ownership (2024)", f"{last_acc:.1f}%", delta="Base Baseline")
    with col2:
        st.metric("Forecast 2027", f"{fc_acc_27:.1f}%", delta=f"+{(fc_acc_27 - last_acc):.1f} pp")
    with col3:
        st.metric("Mobile Money (2024)", f"{last_mm:.1f}%", delta="High Growth Segment")
    with col4:
        st.metric("Telebirr Users", f"{telebirr_users/1e6:.1f}M", delta="Registered Accounts")

    st.markdown("---")
    
    # Progress Bar to 2027 Goal
    st.subheader("Progress toward 60% Inclusion Goal")
    progress_val = min(last_acc / 60.0, 1.0)
    st.progress(progress_val)
    st.caption(f"Current: {last_acc:.1f}% | Target: 60.0% | Status: {'✅ On Track' if fc_acc_27 > 60 else '⚠️ At Risk'}")

# ==========================================
# 5. PAGE: TREND ANALYSIS
# ==========================================
elif menu == "📉 Trend Analysis":
    st.title("Market Dynamics & Anomalies")
    
    tab1, tab2 = st.tabs(["The Telebirr Paradox", "Infrastructure Ceiling"])
    
    with tab1:
        st.markdown("### The Gap Between Registration and Usage")
        st.markdown("While App downloads (Telebirr) skyrocketed, official World Bank account ownership grew slowly. This suggests many users are registered but not 'banked' in the traditional sense.")
        
        fig = go.Figure()
        
        # Access Line
        acc_data = hist_df[hist_df['indicator_code'] == 'ACC_OWNERSHIP']
        fig.add_trace(go.Scatter(
            x=acc_data['observation_date'], y=acc_data['value_numeric'],
            name="Account Ownership (%)", line=dict(color='#2c3e50', width=4)
        ))
        
        # Telebirr Line (Secondary Axis)
        tb_data = hist_df[hist_df['indicator_code'] == 'USG_TELEBIRR_USERS']
        fig.add_trace(go.Scatter(
            x=tb_data['observation_date'], y=tb_data['value_numeric'],
            name="Telebirr Users (Raw Count)", line=dict(color='#e67e22', dash='dot'),
            yaxis="y2"
        ))
        
        fig.update_layout(
            yaxis=dict(title="Ownership %"),
            yaxis2=dict(title="Users (Count)", overlaying="y", side="right"),
            legend=dict(x=0, y=1.1, orientation="h"),
            height=500
        )
        st.plotly_chart(fig, use_container_width=True)

    with tab2:
        st.markdown("### The Mobile Ceiling")
        st.markdown("Financial inclusion cannot easily exceed mobile phone penetration. The two metrics track closely.")
        
        # Compare Ownership vs Mobile Pen
        mob_pen = hist_df[hist_df['indicator_code'].astype(str).str.contains('MOBILE_PEN', case=False)]
        
        fig2 = px.line(hist_df[hist_df['indicator_code'].isin(['ACC_OWNERSHIP'])], 
                       x='observation_date', y='value_numeric', title="Growth Trajectory")
        
        if not mob_pen.empty:
            fig2.add_trace(go.Scatter(x=mob_pen['observation_date'], y=mob_pen['value_numeric'], name="Mobile Penetration", line=dict(color='red', dash='dash')))
            
        st.plotly_chart(fig2, use_container_width=True)

# ==========================================
# 6. PAGE: FORECAST ENGINE
# ==========================================
elif menu == "🔮 Forecast Engine":
    st.title("Interactive Forecast Model (2025-2027)")
    
    col_ctrl1, col_ctrl2 = st.columns(2)
    
    with col_ctrl1:
        target_map = {
            'ACC_OWNERSHIP': 'Access (Account Ownership)',
            'ACC_MM_ACCOUNT': 'Usage (Mobile Money)'
        }
        selected_target = st.selectbox("Select Indicator", list(target_map.keys()), format_func=lambda x: target_map[x])
    
    with col_ctrl2:
        scenario = st.selectbox("Scenario", ["Base Case (Trend + Shock)", "Optimistic (Policy Success)", "Pessimistic (Stagnation)"])

    # Prepare Data
    hist_subset = hist_df[hist_df['indicator_code'] == selected_target]
    fc_subset = fc_df[fc_df['indicator'] == selected_target].copy()
    
    # Apply Dashboard-Side Scenario Logic (Visual adjustment)
    # Note: The CSV contains 'Base', 'Lower_CI' (Pessimistic), 'Upper_CI' (Optimistic)
    # We map the UI selection to which line we highlight
    
    fig_fc = go.Figure()
    
    # 1. Historical
    fig_fc.add_trace(go.Scatter(
        x=hist_subset['observation_date'], y=hist_subset['value_numeric'],
        mode='lines+markers', name='Historical', line=dict(color='black', width=3)
    ))
    
    # 2. Forecast Lines based on selection
    # Convert year to date
    fc_subset['date'] = pd.to_datetime(fc_subset['year'].astype(str) + '-12-31')
    
    if scenario == "Base Case (Trend + Shock)":
        y_val = fc_subset['value']
        color = '#27ae60'
        show_fan = True
    elif scenario == "Optimistic (Policy Success)":
        y_val = fc_subset['upper_ci'] # Visualize the upper bound as the main line
        color = '#2980b9'
        show_fan = False
    else:
        y_val = fc_subset['lower_ci'] # Visualize the lower bound
        color = '#c0392b'
        show_fan = False

    fig_fc.add_trace(go.Scatter(
        x=fc_subset['date'], y=y_val,
        mode='lines+markers', name=f'Forecast ({scenario})', 
        line=dict(color=color, dash='dash', width=3)
    ))
    
    # 3. Fan (Confidence Interval) - Only show in Base Case
    if show_fan:
        fig_fc.add_trace(go.Scatter(
            x=pd.concat([fc_subset['date'], fc_subset['date'][::-1]]),
            y=pd.concat([fc_subset['upper_ci'], fc_subset['lower_ci'][::-1]]),
            fill='toself', fillcolor=color, opacity=0.2, line=dict(color='rgba(255,255,255,0)'),
            name='Confidence Interval'
        ))

    # Add Annotations
    final_val = y_val.iloc[-1]
    fig_fc.add_annotation(
        x=fc_subset['date'].iloc[-1], y=final_val,
        text=f"{final_val:.1f}%", showarrow=True, arrowhead=1
    )

    fig_fc.update_layout(
        title=f"Projection: {target_map[selected_target]}",
        yaxis_title="Percentage (%)",
        yaxis_range=[0, 100],
        height=550
    )
    st.plotly_chart(fig_fc, use_container_width=True)
    
    with st.expander("View Forecast Data Table"):
        st.dataframe(fc_subset[['year', 'value', 'lower_ci', 'upper_ci']].rename(columns={'value': 'Base', 'lower_ci': 'Pessimistic', 'upper_ci': 'Optimistic'}))

# ==========================================
# 7. PAGE: POLICY INSIGHTS
# ==========================================
elif menu == "📋 Policy Insights":
    st.title("Strategic Recommendations")
    
    st.markdown("""
    ### 1. The "60% Goal" is Achievable
    Our models predict that Account Ownership will reach **64.4% by 2027**, surpassing the National Financial Inclusion Strategy target. This is driven by the structural break caused by M-Pesa's entry and continued Telebirr expansion.
    
    ### 2. Focus on "Active Usage"
    While **Access** is solved (trend is positive), **Usage** lags. 
    - Gap: 49% have accounts, but only ~9.5% use Mobile Money actively.
    - **Recommendation:** Policy should shift from "Account Opening" incentives to "Transaction Utility" (e.g., digitizing government payments, merchant interoperability).
    
    ### 3. The Infrastructure Constraint
    Financial inclusion is currently capped by Mobile Penetration (~64%). 
    - **Insight:** You cannot bank someone who doesn't have a phone.
    - **Recommendation:** 4G handset financing and rural tower investment are now *financial inclusion* policies.
    """)
    
    st.info("Report generated by Selam Analytics Forecasting Engine (v1.0)")