
knowledge_base = {
    "loan": "We offer various types of loans including personal loans, home loans, and business loans. What type of loan are you interested in?",
    "interest rate": "Our current interest rates vary depending on the product and your credit score. Please visit our website or contact a representative for more details.",
    "account": "We provide different account types: savings, checking, and investment accounts. How can I help you with your account?",
    "credit card": "We have a range of credit cards with different benefits. Do you want to know about rewards, low interest, or travel cards?",
    "mortgage": "For mortgage inquiries, we can help you with pre-approvals, refinancing, and understanding different loan terms.",
    "investment": "We offer investment advisory services, mutual funds, stocks, and bonds. Are you looking for short-term or long-term investment options?",
    "contact": "You can contact us via phone at 1-800-FINANCE, email at support@financebot.com, or visit our nearest branch.",
    "hours": "Our customer service hours are Monday to Friday, 9 AM to 5 PM EST.",
    "thank you": "You're welcome! Is there anything else I can assist you with?",
    "bye": "Goodbye! Have a great day."
}

def get_response(user_input):
    """Finds the most relevant response based on keywords in the user's input."""
    user_input = user_input.lower()
    for keyword, response in knowledge_base.items():
        if keyword in user_input:
            return response
    return "I'm sorry, I don't understand that. Can you please rephrase your question or ask about loans, accounts, credit cards, or investments?"

# Chatbot interaction loop
print("Hello! I am your financial assistant. How can I help you today? (Type 'bye' to exit)")

while True:
    user_message = input("You: ")
    if user_message.lower() == 'bye':
        print(get_response(user_message))
        break
    
    response = get_response(user_message)
    print(f"Bot: {response}")
