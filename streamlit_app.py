import pandas as pd
import streamlit as st

import requests

# ฟังก์ชันสำหรับส่งการแจ้งเตือนผ่าน LINE Notify
def send_line_notify(message, token):
    url = "https://notify-api.line.me/api/notify"
    headers = {"Authorization": f"Bearer {token}"}
    payload = {"message": message}
    response = requests.post(url, headers=headers, data=payload)
    return response.status_code == 200




st.set_page_config(layout="wide")

# Selectbox



fileContent = ["","python101.md","python102.md","python103.md","PythonForDataSci101.md",
               "game101.md","PythonForApplications101.md","MathByCodingInPython101.md",
               "FinCodeforNewGen101.md"]
listCourse = ["<กรุณาเลือกคอร์สเรียน>",
                                     "Python For New Gen101", 
                                     "Python For New Gen102", 
                                     "Python For New Gen103",
                                     "Python Game 2D 101",
                                     "Python For Data Sci 101",
                                     "Python Application 101",
                                     "Python for Math ตลุยโจทย์ O-NET และสสวท.",
                                     "FinCode for New Gen 101"]

st.subheader("Python Courses")
option = st.selectbox("เลือกรายการ",listCourse , key="selectbox")

# เมื่อเปลี่ยนค่าใน Selectbox จะเปลี่ยนสถานะของ expander
st.session_state.expand_state = False
details = ''
if st.session_state.selectbox:
    st.session_state.expand_state = True

if option=="<กรุณาเลือกคอร์สเรียน>":
   option = ''     

for i,j in zip(listCourse,fileContent):
    # แสดงรายละเอียดใน expander ตามค่าใน selectbox
    if option == i:
        with open(j, "r", encoding="utf-8") as file:
            details = file.read()


# Expander สำหรับแสดงเนื้อหาที่เปลี่ยนแปลงตาม option
with st.expander(f"รายละเอียดเนื้อหา: {option}", expanded=st.session_state.expand_state):
    st.markdown(details)

# Set the title of the form
st.subheader("ฟอร์มสมัครเรียน")

# Create the form
with st.form("registration_form"):
    nickname = st.text_input("ชื่อเล่น:")
    courses = st.text_input("คอร์สเรียน:",value=option)
    mobile = st.text_input("เบอร์มือถือ:")
    line_id = st.text_input("Line ID:")
    
    # Submit button
    submitted = st.form_submit_button("🚀ส่ง Line แจ้งเตือน")
    
    # Handle form submission
    if submitted:
        if nickname and courses and mobile and line_id:
            # ส่งการแจ้งเตือนผ่าน LINE
            line_token = "KcuAS1Q4ZkkwsOdpoxiUM84CBAkTPUIKkBNRitozIfl"  # แทนที่ด้วย Token ของคุณ
            notify_message = f"📌แจ้งเตือนใหม่จากฟอร์ม:\nชื่อ: {nickname}\nสมัคร:{courses} \nmobile: {mobile}\nline_id: {line_id}"
            if send_line_notify(notify_message, line_token):
                st.success("ส่งข้อมูลและแจ้งเตือนผ่าน LINE สำเร็จ!")
            else:
                st.error("เกิดข้อผิดพลาดในการส่งแจ้งเตือน LINE")
        else:
            st.error("กรุณากรอกข้อมูลให้ครบถ้วน")





# Sidebar
st.sidebar.image("logo.png", use_column_width=True)
st.sidebar.header("About")
st.sidebar.markdown(
    "[Asiamediasoft](https://www.facebook.com/asiamediasoft.training) อบรมเรียน Python สอนเขียนโปรแกรมสำหรับน้องๆ ระดับชั้นมัธยม"
)

st.sidebar.header("ติดต่อสอบถาม")
st.sidebar.markdown(
    """
- [LineID](https://line.me/ti/p/0659925697) : 0659925697
- [Youtube](https://www.youtube.com/@tapattan) : @tapattan
- [Mobile](tel:0659925697) : 0659925697
"""
)
 
 