# Import Libraries
import pandas as pd
from chatterbot import ChatBot
from chatterbot.trainers import ListTrainer

# Load Cryptocurrency Dataset
df = pd.read_csv("crypto_data.csv")  # Ensure the dataset contains price trends & sustainability metrics

# Define Rule-Based Investment Analysis
def assess_crypto(price_change, energy_efficiency):
    if price_change > 5 and energy_efficiency > 8:
        return "✅ High potential investment!"
    elif price_change > 5:
        return "⚠️ Profitable, but sustainability is a concern."
    else:
        return "❌ Consider alternative investments."

# Set Up the Chatbot
chatbot = ChatBot("Crypto Advisor")
trainer = ListTrainer(chatbot)

# Train the Chatbot
trainer.train([
    "Which crypto is best?",
    "Let's analyze the data!",
    "Tell me about Bitcoin",
    "Bitcoin is popular but check sustainability.",
    "Is Ethereum a good investment?",
    "Ethereum has strong potential but review market trends."
])

# Function to Get Crypto Advice
def get_crypto_advice(crypto_name):
    crypto_data = df[df['name'] == crypto_name]  # Fetch crypto details from dataset
    if crypto_data.empty:
        return "Crypto not found in the dataset."
    
    price_change = crypto_data['price_change'].values[0]
    energy_efficiency = crypto_data['energy_efficiency'].values[0]
    
    return assess_crypto(price_change, energy_efficiency)

# Run the Chatbot
while True:
    user_input = input("Ask about a cryptocurrency or type 'exit' to quit: ")
    if user_input.lower() == "exit":
        break
    elif "analyze" in user_input.lower():
        crypto_name = user_input.split()[-1]
        print(get_crypto_advice(crypto_name))
    else:
        print(chatbot.get_response(user_input))