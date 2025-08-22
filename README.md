# Whatsapp-Chat-Analyzer

This project uses Python to analyze your WhatsApp chat history and generate visualizations about your conversation, such as message counts, activity times, and most used words.

## How to Use

### 1. Prerequisites
Make sure you have Python installed. Then, install the required libraries by running this command in your terminal:
```bash
pip install pandas matplotlib seaborn wordcloud regex emoji
```

### 2. Export Your WhatsApp Chat
Go to the desired chat in WhatsApp, tap on the options (three dots), select "More," and then "Export chat." Choose **"Without Media"** to get a `.txt` file.

### 3. Add Your Chat File
**IMPORTANT:** Save the exported `.txt` file in the same folder as the scripts and name it exactly `_chat.txt`.

If you want to use a different name, you must open the `main.py` file and change the `CHAT_FILE_PATH` variable to match your filename.
```python
# In main.py
CHAT_FILE_PATH = 'your_chat_file_name.txt' 
```

### 4. Run the Analysis
Open your terminal or command prompt in the project folder and run:
```bash
python main.py
```
The script will then process your chat data and display the visualizations.

## Project Files
*   `main.py`: The main script you run to start the analysis.
*   `parser.py`: Responsible for parsing the raw WhatsApp `.txt` file into structured data.
*   `analyzer.py`: Contains the functions that generate the plots, heatmap, and word cloud.