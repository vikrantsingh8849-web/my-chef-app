import streamlit as st
from groq import Groq

# 1. Page Configuration
st.set_page_config(
    page_title="ChefAI - Master of the Kitchen",
    page_icon="🍳",
    layout="centered"
)

# 2. App Title & UI
st.title("🍳 ChefAI")
st.write("Type any dish or ingredients, and I'll give you a professional recipe.")

# 3. Sidebar for API Key
st.sidebar.header("🔑 API Settings")
api_key = st.sidebar.text_input(
    "Paste your Groq API Key",
    type="password"
)

# 4. Input Area
user_input = st.text_input("What's on the menu?", placeholder="e.g., Butter Chicken or just 'eggs and bread'")

if st.button("👨‍🍳 Get Recipe"):
    if not api_key:
        st.error("Please enter your Groq API Key in the sidebar!")
    elif not user_input:
        st.warning("Tell the Chef what you want to cook!")
    else:
        try:
            client = Groq(api_key=api_key)
            
            # This is where we inject the "Chef Brain" instructions
            response = client.chat.completions.create(
                model="llama3-8b-8192",
                messages=[
                    {
                        "role": "system", 
                        "content": "You are ChefAI, a world-class culinary expert. Provide a structured recipe with a title, prep/cook time, bulleted ingredients, numbered steps, and one pro-tip. Be encouraging and direct."
                    },
                    {"role": "user", "content": f"How do I make: {user_input}"}
                ],
                temperature=0.7 # Adds a bit of culinary creativity!
            )

            # Display the result in a nice box
            st.markdown("---")
            st.success(f"### 🍽️ Your Recipe for {user_input}")
            st.write(response.choices[0].message.content)

        except Exception as e:
            st.error(f"Error: {e}")

st.markdown("---")
st.caption("Free AI Tool powered by Groq & Streamlit")
