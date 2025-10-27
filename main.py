from textblob import TextBlob

text = input("Enter a sentence to analyze: ")
blob = TextBlob(text)
sentiment_score = blob.sentiment.polarity

print("\nSentiment Analysis Result:")
print(f"Sentiment Score: {sentiment_score:.2f}")

if sentiment_score > 0:
    print("🙂 Positive Sentiment")
elif sentiment_score < 0:
    print("☹️ Negative Sentiment")
else:
    print("😐 Neutral Sentiment")

percentage = abs(sentiment_score) * 100
print(f"Confidence: {percentage:.1f}%")
