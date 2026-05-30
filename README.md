# ✈️ Agentic AI-Based Travel Planning Assistant Using LangChain

## 👨‍💻 About Me

Hi, I'm **Updesh Chauhan**, an aspiring Software Development Engineer and AI enthusiast with a strong interest in Python, Machine Learning, and Agentic AI systems.

I enjoy building practical AI applications that solve real-world problems and help users make better decisions. This project was developed as part of my journey to learn LangChain, Large Language Models (LLMs), API integration, and AI-powered automation.

---

# 🌍 Project Overview

**Project Name:** Agentic AI-Based Travel Planning Assistant Using LangChain

**Project Type:** AI / Travel Planning / Agentic AI

This project is an intelligent travel planning assistant that helps users create personalized travel itineraries based on their source city, destination, budget, travel duration, and travel preferences.

Instead of manually searching for flights, hotels, weather forecasts, and tourist attractions across multiple websites, users can simply provide their travel details and receive a complete travel plan in seconds.

The system combines:

* Flight recommendations
* Hotel suggestions
* Tourist attractions
* Live weather forecasts
* Budget estimation
* Day-wise itinerary planning

into a single AI-powered travel experience.

---

# 🎯 Problem Statement

Planning a trip often requires visiting multiple websites to compare flights, hotels, attractions, and weather conditions.

This process can be time-consuming and overwhelming, especially when trying to stay within a budget.

This project aims to simplify travel planning by providing a centralized AI-powered solution that automatically gathers information and generates a complete travel itinerary.

---

# 🚀 Key Features

### Flight Search

Finds available flights between selected cities and recommends the most suitable option.

### Hotel Recommendation

Suggests hotels based on budget, ratings, and travel preferences.

### Tourist Attraction Discovery

Recommends attractions based on destination and user interests.

### Live Weather Forecast

Uses the Open-Meteo API to fetch real-time weather information.

### Budget Estimation

Calculates total trip expenses including:

* Flights
* Hotels
* Food
* Local Transportation

### Day-wise Itinerary Generation

Creates a structured travel schedule for each day of the trip.

### Interactive Streamlit Interface

Provides a simple and user-friendly web interface.

---

# 🛠️ Technologies Used

### Programming Language

* Python

### AI & LLM

* Hugging Face
* LangChain

### Frontend

* Streamlit

### APIs

* Open-Meteo Weather API

### Data Storage

* JSON Files

### Version Control

* Git
* GitHub

---

# 📂 Project Structure

```text
travel_ai_agent/
│
├── app.py
├── agent.py
├── requirements.txt
├── .env.example
│
├── data/
│   ├── flights.json
│   ├── hotels.json
│   └── places.json
│
└── tools/
    ├── flight_tool.py
    ├── hotel_tool.py
    ├── places_tool.py
    ├── weather_tool.py
    └── budget_tool.py
```

# ⚡ Challenges Faced During Development

Building this project was a great learning experience, but I encountered several challenges along the way.

### 1. LangChain Compatibility Issues

Different LangChain versions had different agent implementations. Some methods were deprecated or unavailable, which required adapting the code to newer approaches.

### 2. Hugging Face Model Integration

While integrating Hugging Face models, I encountered issues related to unsupported tasks and model configurations. Several models were tested before finding a stable solution.

### 3. Agent Workflow Design

Creating a system that could intelligently combine flights, hotels, weather, attractions, and budget estimation into a single travel plan required careful planning and modular tool development.

### 4. Data Formatting

The initial output displayed raw Python dictionaries and lists, making the user experience poor. Additional formatting logic was implemented to present information in a cleaner and more readable way.

### 5. Weather API Integration

Handling API responses, location coordinates, and error scenarios required additional validation and exception handling.

### 6. Git & GitHub Issues

Managing repositories, remote configurations, merge conflicts, and deployment workflows provided valuable hands-on experience with version control.

---

# 📖 How to Run This Project

## Step 1: Clone Repository

```bash
git clone <repository-url>
```

## Step 2: Move into Project Directory

```bash
cd travel_ai_agent
```

## Step 3: Install Dependencies

```bash
pip install -r requirements.txt
```

## Step 4: Create Environment File

Create a file named:

```text
.env
```

Add your Hugging Face token:

```env
HUGGINGFACEHUB_API_TOKEN=your_token_here
```

## Step 5: Run Application

```bash
streamlit run app.py
```

## Step 6: Open Browser

Streamlit will automatically provide a local URL such as:

```text
http://localhost:8501
```

Open it in your browser.

---

# 💡 How to Use

1. Select your source city.
2. Select your destination.
3. Choose the number of travel days.
4. Enter your budget.
5. Select your travel preference.
6. Click **Generate Trip Plan**.
7. Review the generated itinerary, hotel recommendations, weather forecast, and budget estimation.

---

# 🔮 Future Improvements

Some features I would like to add in future versions:

* Real-time flight APIs
* Real-time hotel booking APIs
* Multiple destination planning
* Google Maps integration
* PDF itinerary download
* Travel cost optimization
* User authentication
* Voice-based travel planning
* Chatbot interface
* Multi-language support

---

# 📚 Learning Outcomes

Through this project, I gained practical experience in:

* Agentic AI systems
* LangChain architecture
* Prompt engineering
* API integration
* Streamlit development
* JSON data processing
* Error handling
* Git & GitHub workflows
* Building end-to-end AI applications

---

# 🙏 Thank You

Thank you for visiting this repository.

If you find this project useful, feel free to explore the code, suggest improvements, or contribute to future enhancements.
