import streamlit as st
from PIL import Image


st.write('''
# my blog
''')
st.write('**My Journey as a Computer Engineering Student In this technological era, We cannot imagine our world now a days without internet as this mingled with our daily life very much and this is inseparable from us.Today mans scientific knowledge is very wide advanced. In this generation the understanding and adaptation to things is bearly needed. Computers give humans a comfort on their needs and helps them to fulfill tasks. Jobs and opportunities in It industry is highly in demand. .**')

col1, col2 = st.columns(2)

with col1:
   st.image("mike.jpg") 

with col2:
   st.image("poliran.jpg")

st.write("As my progress in my computer engineering studies, I have the opportunity to delve into specialized areas that align with your interests and aspirations. Whether it's the intricate world of microprocessors, the vast domain of computer networks, or the ever-expanding realm of software developing ,  and discover the niche that ignites my passion.")   

st.markdown('## about me', unsafe_allow_html=True)
st.info('''
- Mike Bryan A. Poliran. 18 years Old.
- BSCpE 1A. 
- Surigao del norte state university.
- Brgy. Magsaysay, Placer SDN.
- Poliranmikebryan@gmail.com
- Facebook: Mike Poliran
''')
st.title("")
st.write("My journey as a computer engineering student has been a transformative experience, shaping my perspectives and opening up a world of possibilities. I have learned not only the technical skills required to become a competent engineer but also the resilience, perseverance, and creativity essential for success in this ever-evolving field.")


