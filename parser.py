import regex as re
import pandas as pd
import emoji

def parse_chat(file_path):
    """
    Parses a WhatsApp chat export file into a Pandas DataFrame.
    """
    with open(file_path, 'r', encoding='utf-8') as file:
        chat_text = file.read()

    # Regex to capture date, time, author, and message
    # This pattern matches the "DD/MM/YYYY, HH:MM - Author: Message" format
    pattern = re.compile(r"(\d{1,2}/\d{1,2}/\d{2,4}), (\d{1,2}:\d{2}) - ([^:]+): (.*)")
    
    matches = pattern.findall(chat_text)
    
    data = []
    for match in matches:
        date, time, author, message = match
        data.append({
            'Date': date,
            'Time': time,
            'Author': author.strip(),
            'Message': message.strip()
        })
        
    df = pd.DataFrame(data)
    
    # This format string matches your "DD/MM/YYYY HH:MM" structure exactly
    df['DateTime'] = pd.to_datetime(df['Date'] + ' ' + df['Time'], format='%d/%m/%Y %H:%M')
    
    # Add useful time-based columns
    df['Hour'] = df['DateTime'].dt.hour
    df['DayOfWeek'] = df['DateTime'].dt.day_name()
    
    print("Chat data parsed successfully!")
    return df