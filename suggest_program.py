import streamlit as st
import os

def calculate_percentage(marks_obtained, total_marks):
    return (marks_obtained / total_marks) * 100

def get_visitor_count():
    if not os.path.exists("visitor_count.txt"):
        with open("visitor_count.txt", "w") as f:
            f.write("0")
    with open("visitor_count.txt", "r") as f:
        count = int(f.read().strip())
    return count

def increment_visitor_count():
    count = get_visitor_count() + 1
    with open("visitor_count.txt", "w") as f:
        f.write(str(count))
    return count

def main():
    st.markdown(
        """
        <style>
        .main-title {
            background-color: #4CAF50; /* Header background color */
            color: white;
            padding: 10px;
            text-align: center;
        }
        .footer {
            position: fixed;
            left: 0;
            bottom: 0;
            width: 100%;
            background-color: #f44336; /* Footer background color */
            color: white;
            text-align: center;
            padding: 10px;
        }
        .suggestion {
            color: #FF5733;
            font-weight: bold;
        }
        .visitor-counter {
            position: fixed;
            top: 50%;
            right: 10px;
            background-color: #4CAF50;
            color: white;
            padding: 10px;
            border-radius: 5px;
            transform: translateY(-50%);
        }
        </style>
        """,
        unsafe_allow_html=True
    )

    st.markdown('<h1 class="main-title">Student Marks and Career Suggestions</h1>', unsafe_allow_html=True)
    
    visitor_count = increment_visitor_count()
    st.markdown(f'<div class="visitor-counter">Total Visitors: {visitor_count}</div>', unsafe_allow_html=True)
    
    # Initialize session state for inputs
    if "reset" not in st.session_state:
        st.session_state.reset = False

    def reset_form():
        st.session_state.reset = True
        st.experimental_rerun()

    if st.session_state.reset:
        metric_math = 0
        metric_english = 0
        metric_biology = 0
        metric_chemistry = 0
        metric_computer = 0
        intermediate_math = 0
        intermediate_english = 0
        intermediate_biology = 0
        intermediate_chemistry = 0
        intermediate_computer = 0
        st.session_state.reset = False
    else:
        metric_math = st.number_input("Metric Math:", min_value=0, max_value=150, value=0)
        metric_english = st.number_input("Metric English:", min_value=0, max_value=150, value=0)
        metric_biology = st.number_input("Metric Biology:", min_value=0, max_value=150, value=0)
        metric_chemistry = st.number_input("Metric Chemistry:", min_value=0, max_value=150, value=0)
        metric_computer = st.number_input("Metric Computer:", min_value=0, max_value=150, value=0)
        intermediate_math = st.number_input("Intermediate Math:", min_value=0, max_value=150, value=0)
        intermediate_english = st.number_input("Intermediate English:", min_value=0, max_value=150, value=0)
        intermediate_biology = st.number_input("Intermediate Biology:", min_value=0, max_value=150, value=0)
        intermediate_chemistry = st.number_input("Intermediate Chemistry:", min_value=0, max_value=150, value=0)
        intermediate_computer = st.number_input("Intermediate Computer:", min_value=0, max_value=150, value=0)

    if st.button("Submit"):
        metric_subjects = {
            "Math": metric_math,
            "English": metric_english,
            "Biology": metric_biology,
            "Chemistry": metric_chemistry,
            "Computer": metric_computer
        }

        intermediate_subjects = {
            "Math": intermediate_math,
            "English": intermediate_english,
            "Biology": intermediate_biology,
            "Chemistry": intermediate_chemistry,
            "Computer": intermediate_computer
        }

        st.header("Subject Percentages:")
        
        math_percentage = calculate_percentage(metric_math + intermediate_math, 300)
        st.write(f"Math (Metric + Intermediate): {math_percentage:.2f}%")
        
        english_percentage = calculate_percentage(metric_english + intermediate_english, 300)
        st.write(f"English (Metric + Intermediate): {english_percentage:.2f}%")
        
        biology_percentage = calculate_percentage(metric_biology + intermediate_biology, 300)
        st.write(f"Biology (Metric + Intermediate): {biology_percentage:.2f}%")
        
        computer_percentage = calculate_percentage(metric_computer + intermediate_computer, 300)
        st.write(f"Computer (Metric + Intermediate): {computer_percentage:.2f}%")

        st.header("Career Suggestions:")

        if computer_percentage >= 80:
            st.markdown('<p class="suggestion">Welcome to Computer Science, Information Technology, Artificial Intelligence, Cyber Security!</p>', unsafe_allow_html=True)

        if english_percentage >=80:
            st.markdown('<p class="suggestion">You may consider pursuing BS English.</p>', unsafe_allow_html=True)

        if math_percentage >= 80:
            st.markdown('<p class="suggestion">You may consider pursuing Data Science and Artificial Intelligence.</p>', unsafe_allow_html=True)

        if biology_percentage >= 90:
            st.markdown('<p class="suggestion">You may consider pursuing Medical (MBBS).</p>', unsafe_allow_html=True)

        if (math_percentage >=80 and calculate_percentage(metric_chemistry + intermediate_chemistry, 300) > 80):
            st.markdown('<p class="suggestion">You may consider pursuing Engineering.</p>', unsafe_allow_html=True)

    if st.button("Clear"):
        reset_form()

    st.markdown('<div class="footer">نوجوانان سیت پور</div>', unsafe_allow_html=True)

if __name__ == "__main__":
    main()
