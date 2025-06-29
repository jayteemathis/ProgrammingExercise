#returns a list of 30 common spam keywords and phrases
def get_spam_keywords():
    return [
        "free", "congratulations", "winner", "act now", "limited time",
        "urgent", "money back", "click here", "risk-free", "guarantee",
        "amazing", "credit card", "call now", "exclusive deal", "extra cash",
        "earn money", "no cost", "offer expires", "apply now", "cheap",
        "discount", "eliminate debt", "investment", "work from home", "miracle",
        "get paid", "double your income", "lose weight", "meet singles", "cash bonus"
    ]

#scans the user's email message for spam keywords
#calculates the spam score
def scan_message(message, keywords):
    spam_score = 0                #counter for the spam score
    found_keywords = []           #list to hold found spam words

    # change message to lowercase for easier matching
    message_lower = message.lower()

    # around through each keyword and check if it's in the message
    for keyword in keywords:
        if keyword in message_lower:
            spam_score += 1       #add 1 point for each match
            found_keywords.append(keyword)

    return spam_score, found_keywords  # retun score and list of matches

#this function rates the spam score into categories
def get_spam_rating(score):
    if score == 0:
        return "Very Unlikely Spam"
    elif score <= 3:
        return "Low Likelihood of Spam"
    elif score <= 7:
        return "Moderate Likelihood of Spam"
    else:
        return "High Likelihood of Spam"

#the main function ties everything together
def main():
    #get the list of spam keywords
    keywords = get_spam_keywords()

    #ask the user to enter an email message
    user_message = input("Enter your email message:\n")

    #scan the message for spam keywords
    score, found = scan_message(user_message, keywords)

    #get the spam likelihood based on score
    rating = get_spam_rating(score)

    #show the results to the user
    print("\n--- Spam Check Result ---")
    print(f"Spam Score: {score}")
    print(f"Spam Likelihood: {rating}")
    print(f"Spam Words/Phrases Found: {', '.join(found) if found else 'None'}")

#run program
if __name__ == "__main__":
    main()