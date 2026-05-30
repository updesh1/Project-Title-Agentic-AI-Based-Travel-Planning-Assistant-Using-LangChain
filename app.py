import streamlit as st
from agent import plan_trip_with_agent

st.set_page_config(
    page_title="AI Travel Planner",
    page_icon="✈️",
    layout="wide"
)

st.markdown("""
<style>
.main-title {
    font-size: 42px;
    font-weight: 800;
    color: #1f4e79;
}
.subtitle {
    font-size: 18px;
    color: #555;
}
.card {
    background-color: #f8f9fa;
    padding: 20px;
    border-radius: 14px;
    box-shadow: 0px 2px 8px rgba(0,0,0,0.08);
    margin-bottom: 20px;
}
.result-box {
    background-color: #ffffff;
    padding: 25px;
    border-radius: 16px;
    border-left: 6px solid #1f77b4;
}
</style>
""", unsafe_allow_html=True)

st.markdown('<div class="main-title">✈️ Agentic AI Travel Planner</div>', unsafe_allow_html=True)
st.markdown(
    '<div class="subtitle">Plan smart trips using Hugging Face, LangChain-style tools, JSON data, and live weather API.</div>',
    unsafe_allow_html=True
)

st.divider()

with st.sidebar:
    st.header("🧳 Trip Details")

    source = st.selectbox(
    "From",
    ["Delhi", "Mumbai", "Lucknow", "Bangalore", "Hyderabad", "Pune", "Kolkata", "Chennai"]
    )

    destination = st.selectbox(
        "To",
        ["Goa", "Delhi", "Mumbai", "Jaipur", "Agra", "Varanasi", "Lucknow", "Udaipur", "Manali", "Shimla", "Kerala", "Darjeeling"]
    )

    days = st.slider("Trip Duration", 1, 7, 4)

    budget = st.number_input(
        "Budget in ₹",
        min_value=5000,
        max_value=100000,
        value=20000,
        step=1000
    )

    preference = st.selectbox(
        "Travel Preference",
        ["Beach", "Heritage", "Nature", "Historical", "Budget", "Luxury"]
    )

    generate_button = st.button("🚀 Generate Trip Plan", use_container_width=True)

col1, col2, col3, col4 = st.columns(4)

with col1:
    st.markdown('<div class="card"><h4>📍 Source</h4><h3>{}</h3></div>'.format(source), unsafe_allow_html=True)

with col2:
    st.markdown('<div class="card"><h4>🏖 Destination</h4><h3>{}</h3></div>'.format(destination), unsafe_allow_html=True)

with col3:
    st.markdown('<div class="card"><h4>📅 Days</h4><h3>{}</h3></div>'.format(days), unsafe_allow_html=True)

with col4:
    st.markdown('<div class="card"><h4>💰 Budget</h4><h3>₹{}</h3></div>'.format(budget), unsafe_allow_html=True)

st.divider()

if generate_button:
    with st.spinner("Planning your trip..."):
        final_plan = plan_trip_with_agent(
            source=source,
            destination=destination,
            days=days,
            budget=budget,
            preference=preference
        )

    st.success("Trip plan generated successfully!")

    st.markdown("## 🗺 Your AI Travel Plan")
    st.markdown(
        f"""
        <div class="result-box">
        {final_plan.replace(chr(10), "<br>")}
        </div>
        """,
        unsafe_allow_html=True
    )

else:
    st.info("Fill trip details from the sidebar and click Generate Trip Plan.")