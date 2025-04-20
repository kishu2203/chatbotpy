# smart_chatbot.py

def smart_chatbot():
    print("🤖 SmartBot: Hello! I'm your smart assistant. Type 'exit' to end the chat.")

    while True:
        user_input = input("You: ").lower()

        # Exit condition
        if user_input in ["exit", "bye", "quit"]:
            print("🤖 SmartBot: Goodbye! Stay safe and happy! 👋")
            break

        # Greeting
        elif "hello" in user_input or "hi" in user_input:
            print("🤖 SmartBot: Hi there! 👋 How can I assist you today?")
        
        # Asking about wellbeing
        elif "how are you" in user_input:
            print("🤖 SmartBot: I'm doing great! Thanks for asking. How about you?")
        
        # Telling jokes
        elif "joke" in user_input:
            print("🤖 SmartBot: Why don't scientists trust atoms? Because they make up everything! 😄")
        
        # Talking about weather
        elif "weather" in user_input:
            print("🤖 SmartBot: I'm not connected to the weather network yet, but I hope it's sunny wherever you are! ☀️")
        
        # Talking about learning
        elif "learn" in user_input or "study" in user_input:
            print("🤖 SmartBot: Learning is awesome! 📚 What topic are you interested in?")
        
        # Cyber security
        elif "cyber security" in user_input or "security" in user_input:
            print("🤖 SmartBot: Cyber Security is crucial! Stay updated, use strong passwords, and enable multi-factor authentication! 🔒")
        
        # Default fallback
        else:
            print("🤖 SmartBot: Hmm... I didn't get that. Could you ask in another way?")

if __name__ == "__main__":
    smart_chatbot()
