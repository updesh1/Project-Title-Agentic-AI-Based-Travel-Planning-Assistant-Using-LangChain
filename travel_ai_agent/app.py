import streamlit as st
from agent import plan_trip


st.set_page_config(
    page_title="Agentic AI Travel Planner",
    page_icon="✈️",
    layout="wide"
)

st.title("Agentic AI-Based Travel Planning Assistant")
st.write("Plan trips using Hugging Face LLM, LangChain, JSON tools, and live weather API.")

with st.sidebar:
    st.header("Trip Details")

    source = st.selectbox(
        "Source City",
        ["Delhi", "Mumbai", "Lucknow"]
    )

    destination = st.selectbox(
        "Destination City",
        ["Goa"]
    )

    days = st.slider(
        "Number of Days",
        min_value=1,
        max_value=7,
        value=3
    )

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

    generate_button = st.button("Generate Trip Plan")


if generate_button:
    with st.spinner("Generating your travel plan..."):
        result = plan_trip(
            source=source,
            destination=destination,
            days=days,
            budget=budget,
            preference=preference
        )

    st.subheader("Final AI Travel Plan")
    st.write(result["final_response"])

    st.divider()

    col1, col2 = st.columns(2)

    with col1:
        st.subheader("Selected Flight")
        st.json(result["flight"])

        st.subheader("Selected Hotel")
        st.json(result["hotel"])

    with col2:
        st.subheader("Budget Breakdown")
        st.json(result["budget_breakdown"])

        st.subheader("Weather")
        st.json(result["weather"])

    st.subheader("Recommended Places")
    st.json(result["places"])

    st.subheader("Day-wise Itinerary")
    st.json(result["itinerary"])
else:
    st.info("Enter trip details from the sidebar and click Generate Trip Plan.")