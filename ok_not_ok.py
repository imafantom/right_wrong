import streamlit as st

# Data: Sentences, Correctness, and Explanations
sentences_data = [
    {"sentence": "I have saw that movie last week.", "correct": "Wrong",
     "explanation": "Use 'saw' instead of 'have saw' for specific past time."},
    {"sentence": "She hasn’t never traveled abroad.", "correct": "Wrong",
     "explanation": "Avoid double negatives. Correct sentence: 'She has never traveled abroad.'"},
    {"sentence": "Have you finish your homework yet?", "correct": "Wrong",
     "explanation": "Use 'finished' instead of 'finish' as the past participle."},
    {"sentence": "He use to play football every weekend.", "correct": "Wrong",
     "explanation": "Correct form is 'used to.' Add 'd' for past tense."},
    {"sentence": "I didn’t used to like coffee, but now I do.", "correct": "Wrong",
     "explanation": "After 'didn't,' use 'use to' without 'd'."},
    {"sentence": "Did you used to live in London?", "correct": "Wrong",
     "explanation": "After 'did,' use 'use to' without 'd'."},
    {"sentence": "You should studied harder for the exam.", "correct": "Wrong",
     "explanation": "Use 'should have studied' for this structure."},
    {"sentence": "They shouldn’t of gone to the party so late.", "correct": "Wrong",
     "explanation": "Replace 'of' with 'have' to form 'shouldn’t have gone.'"},
    {"sentence": "I should had called her before the meeting.", "correct": "Wrong",
     "explanation": "Replace 'had' with 'have' to form 'should have called.'"},
    {"sentence": "If she would have known, she would have helped.", "correct": "Wrong",
     "explanation": "Use 'had known' in the third conditional."},
    {"sentence": "We could finish the project if we had started earlier.", "correct": "Wrong",
     "explanation": "Use 'could have finished' for the third conditional."},
    {"sentence": "If I had knew about the problem, I would have solved it.", "correct": "Wrong",
     "explanation": "Use 'had known' instead of 'had knew.'"},
    {"sentence": "The cake is baked by my sister yesterday.", "correct": "Wrong",
     "explanation": "Use 'was baked' for past actions in the passive voice."},
    {"sentence": "The book was reading by a student during the lesson.", "correct": "Wrong",
     "explanation": "Correct form is 'was being read' for the past continuous passive."},
    {"sentence": "Have the documents been send to the client?", "correct": "Wrong",
     "explanation": "Use 'sent' instead of 'send' as the past participle."},
    {"sentence": "By the time we arrived, they already ate.", "correct": "Wrong",
     "explanation": "Correct form is 'had already eaten' for the Past Perfect."},
    {"sentence": "She said she has completed the project before the deadline.", "correct": "Wrong",
     "explanation": "Use 'had completed' for reported speech."},
    {"sentence": "He had went home before we could talk to him.", "correct": "Wrong",
     "explanation": "Use 'had gone' instead of 'had went.'"},
    {"sentence": "He must to leave early because of his train.", "correct": "Wrong",
     "explanation": "Remove 'to' after 'must.' Correct sentence: 'He must leave early.'"},
    {"sentence": "You can’t have saw her; she is abroad.", "correct": "Wrong",
     "explanation": "Use 'seen' instead of 'saw' as the past participle."}
]

# Streamlit Application
st.title("Grammar Correction Practice")

st.write("Choose whether each sentence is 'Right' or 'Wrong'. After making a choice, you'll see an explanation!")

# Loop through each sentence
for i, data in enumerate(sentences_data):
    st.subheader(f"Sentence {i+1}:")
    st.write(data["sentence"])

    # User choice: Right or Wrong
    user_choice = st.radio(f"Do you think this sentence is correct?", ["Right", "Wrong"], key=f"choice_{i}")

    # Show explanation based on user choice
    if st.button(f"Submit Answer for Sentence {i+1}", key=f"button_{i}"):
        if user_choice == data["correct"]:
            st.success("Correct!")
        else:
            st.error("Incorrect.")
        st.info(f"Explanation: {data['explanation']}")

st.write("Practice completed? Review explanations and try again if needed!")
