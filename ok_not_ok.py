import streamlit as st
import random

# Data: Sentences, Correctness, and Explanations
sentences_data = [
    {"sentence": "I have saw that movie last week.", "correct": "Wrong",
     "explanation": "Use 'saw' instead of 'have saw' for specific past time."},
    {"sentence": "She hasn’t never traveled abroad.", "correct": "Wrong",
     "explanation": "Avoid double negatives. Correct sentence: 'She has never traveled abroad.'"},
    {"sentence": "He used to play football every weekend.", "correct": "Right",
     "explanation": "This is correct. 'Used to' is the proper form for a past habit."},
    {"sentence": "You should studied harder for the exam.", "correct": "Wrong",
     "explanation": "Use 'should have studied' for this structure."},
    {"sentence": "If she had known, she would have helped.", "correct": "Right",
     "explanation": "This is correct. It follows the structure of the third conditional."},
    {"sentence": "The cake is baked by my sister yesterday.", "correct": "Wrong",
     "explanation": "Use 'was baked' for past actions in the passive voice."},
    {"sentence": "By the time we arrived, they had already eaten.", "correct": "Right",
     "explanation": "This is correct. 'Had already eaten' is the proper past perfect tense."},
    {"sentence": "He must to leave early because of his train.", "correct": "Wrong",
     "explanation": "Remove 'to' after 'must.' Correct sentence: 'He must leave early.'"},
    {"sentence": "She has just arrived at the station.", "correct": "Right",
     "explanation": "This is correct. 'Has just arrived' is the appropriate present perfect structure."},
    {"sentence": "The book was reading by a student during the lesson.", "correct": "Wrong",
     "explanation": "Correct form is 'was being read' for the past continuous passive."},
    {"sentence": "We could finish the project if we had started earlier.", "correct": "Wrong",
     "explanation": "Use 'could have finished' for the third conditional."},
    {"sentence": "I should had called her before the meeting.", "correct": "Wrong",
     "explanation": "Replace 'had' with 'have' to form 'should have called.'"},
    {"sentence": "She never used to drink coffee.", "correct": "Right",
     "explanation": "This is correct. 'Used to' is the proper form for past habits."},
    {"sentence": "The documents have been sent to the client.", "correct": "Right",
     "explanation": "This is correct. 'Have been sent' is the correct passive voice form in present perfect."},
    {"sentence": "If I had knew about the problem, I would have solved it.", "correct": "Wrong",
     "explanation": "Use 'had known' instead of 'had knew.'"},
    {"sentence": "She said she had completed the project before the deadline.", "correct": "Right",
     "explanation": "This is correct. 'Had completed' is appropriate for reported speech."},
    {"sentence": "You can’t have saw her; she is abroad.", "correct": "Wrong",
     "explanation": "Use 'seen' instead of 'saw' as the past participle."},
    {"sentence": "He will finish the project tomorrow.", "correct": "Right",
     "explanation": "This is correct. It uses proper future tense."},
    {"sentence": "They didn’t used to like vegetables.", "correct": "Wrong",
     "explanation": "After 'didn't,' use 'use to' without 'd.'"},
    {"sentence": "Have the documents been send to the client?", "correct": "Wrong",
     "explanation": "Use 'sent' instead of 'send' as the past participle."}
]

# Motivational messages for correct answers
motivational_messages = [
    "Your teacher is impressed!", "You are a grammar ninja!", "You are the best in the world!",
    "You've just made your teacher so proud!", "You're a real hero!", "Outstanding work!",
    "You're unstoppable!", "You're the master of grammar!", "Fantastic effort!",
    "You're acing this!", "You are shining bright!", "Incredible!", "You're on fire!",
    "You're a grammar superstar!", "You're making history!", "Exceptional work!",
    "Grammar genius at work!", "You're a true champion!", "You nailed it!", "Bravo!"
]

# Encouraging messages for incorrect answers
encouraging_messages = [
    "You can do better.", "You've just made your teacher cry.",
    "If you had been right, you would have made a million dollars!",
    "Don't give up; try again!", "Mistakes help you grow!", "Keep practicing, and you'll get it!"
]

# Smiley emoji
smiley_face = "😄"
# Typing cat GIF URL
typing_cat_gif = "https://media.giphy.com/media/JIX9t2j0ZTN9S/giphy.gif"

# Counter for correct answers and points
correct_answers = 0
points = 0

# Loop through all 20 sentences
for i, data in enumerate(sentences_data):
    st.subheader(f"Sentence {i+1}:")
    if f"answered_{i}" not in st.session_state:
        st.markdown(
            f"<span style='font-size: 18px; font-weight: bold;'>{data['sentence']}</span>",
            unsafe_allow_html=True,
        )
        user_choice = st.radio("", ["Right", "Wrong"], key=f"choice_{i}")

        if st.button(f"Submit Answer for Sentence {i+1}", key=f"button_{i}"):
            st.session_state[f"answered_{i}"] = True
            if user_choice == data["correct"]:
                st.success(f"Correct! {smiley_face} {random.choice(motivational_messages)}")
                correct_answers += 1
                points += 1
            else:
                st.error(f"Incorrect. {random.choice(encouraging_messages)}")
            st.info(f"Explanation: {data['explanation']}")
            st.experimental_rerun()

# Completion Message
if len([key for key in st.session_state if key.startswith("answered_")]) == len(sentences_data):
    st.balloons()  # Streamlit balloons for celebration
    st.markdown("### 🎉 Well done! You've completed the practice! 🎉")
    st.image(typing_cat_gif, width=300)

# Final Points Display
st.markdown(f"### Your total points: {points}")
