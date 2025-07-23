# AI Powered Travel Companion

**An intelligent travel assistant designed to streamline your journey with real-time tools and resources**

---

## Overview

AI Travel Companion is a web application built with Streamlit that consolidates essential travel utilities into a single platform. It offers a variety of features aimed at improving your travel planning and experience on the go.

---

## Features

- **Currency Converter**  
  Provides live currency exchange rates to simplify money conversions (implemented in `Currency.py`).

- **Weather Updates**  
  Delivers accurate, location-specific weather forecasts to help plan your trips effectively (powered by `location_weather.py`).

- **Interactive Travel Chatbot**  
  AI-driven chat assistant offering immediate travel advice and support (found in `Chat_botpy`).

- **Resource Library**  
  Houses a collection of travel guides and documents accessible from the `pdfs` directory.

- **Streamlit User Interface**  
  An intuitive and visually appealing web interface (`streamlit_app.py`) that integrates all features seamlessly.

---

## Installation

1. Clone the repository:
   ```bash
   git clone https://github.com/shikhaSingh4934/AI-Powered-Travel-Language-Companion-App.git
   cd AI-Powered-Travel-Language-Companion-App
2. Install dependencies:
   ```bash
   pip install -r requirements.txt

## Usage
Run the Streamlit app locally by executing:
```bash
streamlit run streamlit_app.py
```
## Project Structure
```bash
AI-Powered-Travel-Language-Companion-App/
├── pdfs/                  # Travel guides and documentation
├── Chat_botpy/            # AI chat module
├── Currency.py            # Currency converter
├── location_weather.py    # Weather data fetcher
├── streamlit_app.py       # Main Streamlit app interface
├── LICENSE                # License information
├── README.md              # Project documentation
└── requirements.txt       # Python dependencies
```




