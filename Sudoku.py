import streamlit as st
from PIL import Image
st.set_page_config(page_title="SUDOKU")
st.header("SUDOKU")
st.write('''Welcome! We offer the following difficulty levels in sudoku:
1. Easy
2. Medium
3. Hard ''')
x=st.number_input("Enter the difficulty level",1,3)
if x==1:
    st.write("Solve the puzzle before entering the values as they can be entered only once. All the best!")
    image=Image.open("Easy sudoku.jpg")
    st.image(image, caption="Easy sudoku")
    st.write('''Enter the values  according to the coordinates.
For example, if you are asked the value for box (1,5), it means enter the value for the box on 1st row and 5th column.''')
    col1, col2, col3, col4, col5, col6, col7, col8, col9= st.columns(9)
    with col1:
        a=st.number_input("(1,1)",1,9)
        t=st.number_input("(5,1)",1,9)
        y=st.number_input("(6,1)",1,9)
        ad=st.number_input("(7,1)",1,9)
        ai=st.number_input("(8,1)",1,9)
    with col2:
        b=st.number_input("(1,2)",1,9)
        u=st.number_input("(5,2)",1,9)
        ae=st.number_input("(7,2)",1,9)
        an=st.number_input("(9,2)",1,9)
    with col3:
        C=st.number_input("(1,3)",1,9)
        e=st.number_input("(2,3)",1,9)
        j=st.number_input("(3,3)",1,9)
        o=st.number_input("(4,3)",1,9)
        z=st.number_input("(6,3)",1,9)
        aj=st.number_input("(8,3)",1,9)
    with col4:
        f=st.number_input("(2,4)",1,9)
        k=st.number_input("(3,4)",1,9)
        aa=st.number_input("(6,4)",1,9)
        ak=st.number_input("(8,4)",1,9)
        ao=st.number_input("(9,4)",1,9)
    with col5:
        l=st.number_input("(3,5)",1,9)
        p=st.number_input("(4,5)",1,9)
        v=st.number_input("(5,5)",1,9)
        ab=st.number_input("(6,5)",1,9)
        af=st.number_input("(7,5)",1,9)
    with col6:
        c=st.number_input("(1,6)",1,9)
        g=st.number_input("(2,6)",1,9)
        q=st.number_input("(4,6)",1,9)
        ag=st.number_input("(7,6)",1,9)
        al=st.number_input("(8,6)",1,9)
    with col7:
        h=st.number_input("(2,7)",1,9)
        r=st.number_input("(4,7)",1,9)
        ac=st.number_input("(6,7)",1,9)
        ah=st.number_input("(7,7)",1,9)
        am=st.number_input("(8,7)",1,9)
        ap=st.number_input("(9,7)",1,9)
    with col8:
        d=st.number_input("(1,8)",1,9)
        m=st.number_input("(3,8)",1,9)
        w=st.number_input("(5,8)",1,9)
        aq=st.number_input("(9,8)",1,9)
    with col9:
        i=st.number_input("(2,9)",1,9)
        n=st.number_input("(3,9)",1,9)
        s=st.number_input("(4,9)",1,9)
        x=st.number_input("(5,9)",1,9)
        ar=st.number_input("(9,9)",1,9)
    if a==4 and b==3 and C==5 and c==9 and d==8 and e==2 and f==5 and g==1 and h==4 and i==3 and j==7 and k==8 and l==3 and m==6 and n==2 and o==6 and p==9 and q==5 and r==3 and s==7 and t==3 and u==7 and v==8 and w==1 and x==5 and y==9 and z==1 and aa==7 and ab==4 and ac==6 and ad==5 and ae==1 and af==2 and ag==6 and ah==8 and ai==2 and aj==8 and ak==9 and al==7 and am==1 and an==6 and ao==4 and ap==2 and aq==5 and ar==9:
         st.write("Correct!")
         st.balloons()
    else:
        st.write("Incorrect.... Hard luck!")
        
    
