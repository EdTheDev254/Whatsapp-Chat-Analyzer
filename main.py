from parser import parse_chat
from analyzer import plot_message_counts, generate_word_cloud, plot_activity_heatmap
import matplotlib.pyplot as plt

# --- CONFIGURATION ---
CHAT_FILE_PATH = '_chat.txt'
CHAT_TITLE = "My Friendship Story" # Used for plot titles and saving files

def main():
    # Phase 1: Parse the chat file
    try:
        df = parse_chat(CHAT_FILE_PATH)
        print(f"Loaded {len(df)} total messages.")
    except FileNotFoundError:
        print(f"Error: The file '{CHAT_FILE_PATH}' was not found.")
        print("Please make sure you have exported your chat and named it correctly.")
        return
        
    # Phase 2: Run the analysis and generate plots
    print("Generating visualizations...")
    
    # Plot 1: Who texts more?
    plot_message_counts(df, CHAT_TITLE)
    
    # Plot 2: When do we talk?
    plot_activity_heatmap(df, CHAT_TITLE)

    # Plot 3: What do we talk about?
    generate_word_cloud(df, CHAT_TITLE)
    
    # Display all the plots
    print("Done! Displaying plots.")
    plt.show()

if __name__ == '__main__':
    main()