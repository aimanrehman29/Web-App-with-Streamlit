import streamlit as st

def main():
    st.title("Growth Mindset Challenge")
    st.header("Welcome to the Growth Mindset Web App!")
    st.write("This app is designed to help you adopt a growth mindset and track your personal growth journey.")
    
    st.markdown("""
    **What is a Growth Mindset?**
    
    A growth mindset is the belief that your abilities can be developed through hard work, dedication, and learning from mistakes.
    
    *Embrace Challenges, Learn from Mistakes, Persist, and Celebrate Effort!*
    """)
    
    # Reflection Section
    st.subheader("Reflect on Your Learning")
    reflection = st.text_area("Share your recent challenge and what you learned from it:")
    if st.button("Submit Reflection"):
        if reflection:
            st.success("Thank you for sharing! Keep up the great work!")
        else:
            st.error("Please write something before submitting.")

    # Growth Tracker Section
    st.subheader("Growth Tracker")
    st.write("Set a personal growth goal and track your progress.")
    goal = st.text_input("Enter your growth goal:")
    progress = st.slider("How far along are you in achieving your goal?", 0, 100, 0)
    if st.button("Save Goal"):
        if goal:
            st.write("**Goal:**", goal)
            st.write("**Progress:**", f"{progress}%")
            st.success("Your goal has been saved. Keep pushing forward!")
        else:
            st.error("Please enter a goal before saving.")

    # Daily Inspiration Section
    st.subheader("Daily Inspiration")
    quotes = [
        "The only way to do great work is to love what you do. - Steve Jobs",
        "Don't watch the clock; do what it does. Keep going. - Sam Levenson",
        "It always seems impossible until it's done. - Nelson Mandela",
        "Mistakes are proof that you are trying."
    ]
    
    # Initialize session state for quote index if not already set
    if 'quote_index' not in st.session_state:
        st.session_state.quote_index = 0

    st.write(quotes[st.session_state.quote_index])
    if st.button("Next Quote"):
        st.session_state.quote_index = (st.session_state.quote_index + 1) % len(quotes)
        st.experimental_rerun()

if __name__ == "__main__":
    main()
