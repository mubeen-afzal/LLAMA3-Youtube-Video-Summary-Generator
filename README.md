# LLAMA3-Youtube-Video-Transcript-Generator

## Description
Llama3 Summary Generator is an application designed to streamline your video summarization process. Leveraging the power of Llama3 (LLM) locally deployed and Streamlit for a user-friendly web interface, this tool simplifies the task of extracting concise summaries from YouTube videos.

## Installation and Usage Guide

### 1. Download Ollama
To get started, download Llama3 from the official website [here](https://ollama.com/). Ensure you have the latest version to enjoy all the features and enhancements.

### 2. Setting Up Environment
Create a new virtual environment to isolate dependencies. Once set up, install the necessary packages listed in `requirements.txt`. This ensures a clean and efficient environment tailored for running Llama3 Summary Generator.

```bash
python venv -m myenv
source myenv/bin/activate  # Activate virtual environment
pip install -r requirements.txt
```

### 3. Running the Application
Execute the following command to start the application:

```bash
streamlit run app.py
```

This command initiates the Streamlit server, launching the intuitive web interface for Llama3 Summary Generator.

## Generating Summaries
Once the application is running, simply copy the YouTube video link into the designated input field. With just a click, Llama3 Summary Generator swiftly processes the video content, extracting key insights and presenting them in a succinct summary.

## Key Features
- **Efficiency**: Llama3 Summary Generator harnesses the cutting-edge capabilities of Llama3 (LLM) to rapidly summarize lengthy video content.
- **User-Friendly Interface**: Streamlit provides an intuitive web interface, making it easy for users to interact with the application.
- **Customization**: Users can tailor the summarization process to suit their specific requirements, ensuring relevant and insightful summaries.
- **Local Deployment**: By deploying Llama3 locally, users have full control over the summarization process and data privacy.
