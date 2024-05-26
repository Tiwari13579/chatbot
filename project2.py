# from dotenv import load_dotenv

# load_dotenv()
# import streamlit as st
# import os 
# import google.generativeai as genai 


# os.getenv("GOOGLE_API_KEY")
# genai.configure(api_key=os.getenv("GOOGLE_API_KEY"))

# model=genai.GenerativeModel('gemini-pro')
# chat=model.start_chat(history=[])


# def get_gemini_response(question):
#     response=chat.send_massage(question,stream=True)
#     response_text="".join(chunk.text for chunk in response)
#     return response_text


# st.set_page_config(page_title="Q&A Demo")

# st.header("Your chatbot ")


# if 'chat_history' not in st.session_state:
#     st.session_state['chat_history']=[]


# # button
# input=st.text_input("Input Your question:", key="input")
# submit=st.button("Ask the question")


# if submit and input:
#     response=get_gemini_response(input)
#     st.session_state['chat_history'].append(("you", input, "Bot", response))


# st.subheader("Your chatbot")

# for user_role, user_text,bot_rol, bot_text in st.session_state['chat_history']:
#     with st.container():
#         st.markdown(f"""
#         <div style="padding: 10px; border-radius: 10px; background-color: 
#         #f0f0f5; margin-bottom: 10px; color: #000;">
#             <strong>{user_role}</strong>: {user_text}
#         </div>
#         <div style="padding: 10px; border-radius: 10px; background-color:
#         #e0f7fa; margin-bottom: 10px; color: #000;">
#             <strong>{bot_rol}</strong>: {bot_text}
#         </div>
#         """, unsafe_allow_html=True)
        
        
        
        
from dotenv import load_dotenv
load_dotenv()

import streamlit as st
import os 
import google.generativeai as genai 

os.getenv("GOOGLE_API_KEY")
genai.configure(api_key=os.getenv("GOOGLE_API_KEY"))

model = genai.GenerativeModel('gemini-pro')
chat = model.start_chat(history=[])

def get_gemini_response(question):
    response = chat.send_message(question, stream=True)
    response_text = "".join(chunk.text for chunk in response)
    return response_text

st.set_page_config(page_title="Q&A Demo")
st.header("ChatBot ")

if 'chat_history' not in st.session_state:
    st.session_state['chat_history'] = []

# Button
input_question = st.text_input("Input Your question:", key="input")
submit = st.button("Ask the question")

if submit and input_question:
    response = get_gemini_response(input_question)
    st.session_state['chat_history'].append(("you", input_question, "Bot", response))

st.subheader("Chat History")

chat_html = ""
for user_role, user_text, bot_role, bot_text in st.session_state['chat_history']:
    user_div = f"""<div style="padding: 10px; border-radius: 10px; background-color: #f0f0f5; margin-bottom: 10px; color: #000;">
                    <strong>{user_role}</strong>: {user_text}
                  </div>"""
    bot_div = f"""<div style="padding: 10px; border-radius: 10px; background-color: #e0f7fa; margin-bottom: 10px; color: #000;">
                    <strong>{bot_role}</strong>: {bot_text}
                 </div>"""
    chat_html += user_div + bot_div

st.markdown(chat_html, unsafe_allow_html=True)

        
        
    
            
    



# Bilkul, aapke code ke saare components ko define karke samjha deta hu:

# 1. `load_dotenv()`: Yeh function `.env` file se environment variables ko load karta hai.

# 2. `import streamlit as st`: Streamlit ko `st` ke naam se import karta hai, jo ki interactive web applications banane ke liye istemal hota hai.

# 3. `import os`: `os` module ko import karta hai jo Operating System ke functionalities ko access karne mein madad karta hai.

# 4. `import google.generativeai as genai`: Google ke Generative AI toolkit ko `genai` ke naam se import karta hai.

# 5. `os.getenv("GOOGLE_API_KEY")`: `.env` file se Google API key ko retrieve karta hai.

# 6. `genai.configure(api_key=os.getenv("GOOGLE_API_KEY"))`: Google API key ko use karke Generative AI toolkit ko configure karta hai.

# 7. `model = genai.GenerativeModel('gemini-pro')`: Generative model ko instantiate karta hai, yahaan 'gemini-pro' model ko use kiya gaya hai.

# 8. `chat = model.start_chat(history=[])`: Chat session ko shuru karta hai, jismein `history` parameter mein ek khali list pass ki gayi hai.

# 9. `get_gemini_response(question)`: Function hai jo question ko Generative AI model mein bhejkar uska response laata hai.

# 10. `st.set_page_config(page_title="Q&A Demo")`: Streamlit page ka configuration set karta hai, jismein page ka title set kiya gaya hai.

# 11. `st.header("Your chatbot")`: Ek header ko display karta hai jismein chatbot ka title diya gaya hai.

# 12. `if 'chat_history' not in st.session_state`: Session state mein 'chat_history' key check karta hai aur agar nahi hai to ek khali list use karke set karta hai.

# 13. `input_question = st.text_input("Input Your question:", key="input")`: Text input field ko display karta hai jismein user apna question daal sakta hai.

# 14. `submit = st.button("Ask the question")`: Ek button ko display karta hai jisse user apna question submit kar sakta hai.

# 15. `if submit and input_question`: Agar user ne question submit kiya hai aur vo khali nahi hai, toh Generative AI model se response generate kiya jata hai aur phir chat history mein add kiya jata hai.

# 16. `st.subheader("Chat History")`: Ek subheader ko display karta hai jismein chat history ka title diya gaya hai.

# 17. `chat_html`: Ek string variable hai jismein chat history ka HTML markup stored kiya jata hai.

# 18. `for user_role, user_text, bot_role, bot_text in st.session_state['chat_history']`: Ek loop hai jo chat history ko iterate karta hai aur har message ko user aur chatbot ke role ke saath display karta hai.

# 19. `st.markdown(chat_html, unsafe_allow_html=True)`: HTML markup ko display karta hai jismein chat history shamil hai. `unsafe_allow_html` parameter se HTML ko allow kiya jata hai.

# Yeh hai aapke code ke sabhi components ka overview. Koi bhi aur sawal ho toh poochh sakte hain.