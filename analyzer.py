import matplotlib.pyplot as plt
import seaborn as sns
from wordcloud import WordCloud, STOPWORDS
import emoji

plt.style.use('dark_background')

# Define some default stopwords and add more if you find them in your chat
STOPWORDS.update(['media', 'omitted', 'missed', 'voice', 'call', 'na', 'ni'])

def plot_message_counts(df, title):
    """Plots a bar chart of message counts by author."""
    plt.figure(figsize=(10, 6))
    author_counts = df['Author'].value_counts()
    sns.barplot(x=author_counts.index, y=author_counts.values, palette='viridis')
    plt.title('Total Messages Sent by Each Person')
    plt.xlabel('Author')
    plt.ylabel('Number of Messages')
    plt.xticks(rotation=45)
    plt.tight_layout()
    # plt.savefig(f'{title}_message_counts.png') # Optional: save the plot

def generate_word_cloud(df, title):
    """Generates and displays a word cloud from all messages."""
    text = ' '.join(df['Message'].dropna().str.lower())
    
    plt.figure(figsize=(10, 10))
    wordcloud = WordCloud(
        width=800, 
        height=800,
        background_color='black',
        stopwords=STOPWORDS,
        min_font_size=10
    ).generate(text)
    
    plt.imshow(wordcloud, interpolation='bilinear')
    plt.title('Most Common Words in the Chat')
    plt.axis('off')
    plt.tight_layout()
    # plt.savefig(f'{title}_word_cloud.png')

def plot_activity_heatmap(df, title):
    """Plots a heatmap of chat activity by day of the week and hour."""
    heatmap_data = df.groupby(['DayOfWeek', 'Hour']).size().unstack().fillna(0)
    
    # Order days of the week correctly
    day_order = ['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday', 'Sunday']
    heatmap_data = heatmap_data.reindex(day_order)
    
    plt.figure(figsize=(12, 8))
    sns.heatmap(heatmap_data, cmap='cividis', linewidths=.5)
    plt.title('When Do We Talk? (Activity Heatmap)')
    plt.xlabel('Hour of the Day')
    plt.ylabel('Day of the Week')
    plt.tight_layout()
    # plt.savefig(f'{title}_activity_heatmap.png')