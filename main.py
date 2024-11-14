import streamlit as st
import os
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt


st.title("Welcome Wesley")
st.header("this is a header")
st.subheader("Subheader")
st.markdown("this is a _Markdown_")
st.caption("Small text")
code_example = """
def greet(name):
    print('hello', name)
    """
st.code(code_example, language = "python")

#horizontal line divider
st.divider()

#adding an image
st.image(os.path.join(os.getcwd(), "static", "BG.jfif"))

st.divider()

st.title("Steamlit Elements Demo")

#dataframe section
st.subheader("Dataframe")

df = pd.DataFrame({
    "Name": ["Alice", "Bob", "Charlie", "David"],
    "Age": [25, 32,37, 46],
    "Occupation": ["Engineer", "Doctor", "Artist", "Chef"]
})

st.dataframe(df)

#data editor section (Editable dataframe)
st.subheader("Data Editor")
editable_df = st.data_editor(df) #creating an editable table

#static Table seciton
st.subheader("Static Table")
st.table(df) #creating a static table

#metrics section
st.subheader("Metrics")
st.metric(label = "total Rows", value = len(df))
st.metric(label = "Average Age", value = round(df['Age'].mean(), 1))

st.subheader("JSON and Dctionary")
sample_dict = {
    "Name": "Wesley",
    "Age": 30,
    "Occupation": "Data Scientist",
    "Country": "USA"
}


st.json(sample_dict)

st.divider()
st.title("Streamlit Chart Demo")

#generating sample data
chart_data = pd.DataFrame(
    np.random.randn(20, 3),
    columns = ["A", "B", "C"]
)

#Area Chat column
st.subheader("Area Chart")
st.area_chart(chart_data)


#Bar Cahrt Section
st.subheader("Bar Chart")
st.bar_chart(chart_data)

#line chart
st.subheader("line chart")
st.line_chart(chart_data)

#scatter chart section
st.subheader("Scatter Chart")
scatter_data = pd.DataFrame({
    "X": np.random.randn(1000),
    "Y": np.random.randn(1000)
})

st.scatter_chart(scatter_data)

#Map Section (displaying random points on a map)
st.subheader("Map")
map_data = pd.DataFrame(
    np.random.randn(100,2)/ [50, 50] * [37.75, -122.4], #coordinates around SF
    columns= ['lat', 'lon']
)

st.map(map_data)


st.subheader("pyplot chart")
fig, ax = plt.subplots()
ax.plot(chart_data['A'], label = 'A')
ax.plot(chart_data['B'], label = 'B')
ax.plot(chart_data['C'], label = 'C')
ax.set_title("pyplot line chart")
ax.legend()
st.pyplot(fig)


st.divider()
st.title("Streamlit Form Demo")

with st.form(key = "sample_form"):
    #text input
    st.subheader("text inputs")
    name = st.text_input("Enter your name")
    feedback = st.text_area("Provide your feedback")


    #date and time inputs
    st.subheader("date and time inputs")
    dob = st.date_input("Select Data of Birth", value = pd.to_datetime("today"))
    time = st.time_input("Preferred Time", value = pd.to_datetime("now").time())

    #selectors
    st.subheader("Selector")
    choice = st.radio("Chose an option", ['Option 1', 'Option 2'])
    gender = st.selectbox("Select your gender", ['Male', 'female', 'Other'])
    slider_value = st.select_slider("select a range", options = [1,2,3,4,5])

    #toggles and checkboxes
    st.subheader("toggles and checkboxes")
    notifications = st.checkbox("recveive notifications?")
    toggle_value = st.checkbox("enable dark mode? ", value = False)

    #submit button
    submitted = st.form_submit_button("Submit")


#outside the form

st.divider()

st.title("User Information Form")


form_values = {
    "name": None,
    "height": None,
    "gender": None,
    "dob": None,
    }


with st.form(key  = "user_info_form"):
    form_values["name"] = st.text_input("Enter your name:")
    form_values["gender"] =  st.number_input("Enter you age")
    form_values["height" ] = st.number_input("Enter your height(cm):")
    form_values["dob"] = st.date_input("Enter your date of birth:")


   
    submit_button =  st.form_submit_button()
    print("after submit")
    if submit_button:
            if not all(form_values.values()):
                st.warning("please fill in all of the  fields")
            else:
                 st.balloons()
                 st.write("### Info ")
                 for (key, value ) in form_values.items():
                      st.write(f"{key}: {value}")

