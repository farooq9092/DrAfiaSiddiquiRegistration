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
        body {
            background-image: url('CC.jpg');
            background-size: cover;
            background-repeat: no-repeat;
        }
        .main-title {
            background: linear-gradient(90deg, #4CAF50, #8BC34A); /* Header gradient color */
            color: white;
            padding: 20px;
            text-align: center;
            font-size: 24px;
            border-radius: 5px;
        }
        .mission-statement {
            background: #f5f5f5; /* Light grey background */
            border-left: 5px solid #4CAF50; /* Matching left border */
            padding: 20px;
            margin: 20px 0;
            border-radius: 5px;
            font-size: 16px;
            line-height: 1.5;
        }
        .mission-statement h2 {
            color: #4CAF50; /* Matching color for the title */
        }
        .footer {
            position: fixed;
            left: 0;
            bottom: 0;
            width: 100%;
            background: linear-gradient(90deg, #8BC34A, #4CAF50); /* Footer gradient color */
            color: white;
            text-align: center;
            padding: 10px;
            font-size: 16px;
            border-radius: 5px 5px 0 0;
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
        .social-icons {
            position: fixed;
            top: 50%;
            left: 10px;
            transform: translateY(-50%);
        }
        .social-icons a {
            display: block;
            margin: 10px 0;
        }
        .social-icons img {
            width: 32px;
            height: 32px;
            border-radius: 5px;
            transition: transform 0.2s;
        }
        .social-icons img:hover {
            transform: scale(1.1);
        }
        </style>
        """,
        unsafe_allow_html=True
    )

    st.markdown('<h1 class="main-title">Student Marks and Career Suggestions</h1>', unsafe_allow_html=True)
    
    visitor_count = increment_visitor_count()
    st.markdown(f'<div class="visitor-counter">Total Visitors: {visitor_count}</div>', unsafe_allow_html=True)
    
    st.markdown(
        """
        <div class="social-icons">
            <a href="https://www.youtube.com" target="_blank"><img src="https://upload.wikimedia.org/wikipedia/commons/4/42/YouTube_icon_%282013-2017%29.png" alt="YouTube"></a>
            <a href="https://www.facebook.com/groups/1913020075811796" target="_blank"><img src="https://upload.wikimedia.org/wikipedia/commons/5/51/Facebook_f_logo_%282019%29.svg" alt="Facebook"></a>
            <a href="https://www.instagram.com" target="_blank"><img src="https://upload.wikimedia.org/wikipedia/commons/a/a5/Instagram_icon.png" alt="Instagram"></a>
        </div>
        """,
        unsafe_allow_html=True
    )

    st.markdown(
        """
        <div class="mission-statement">
            <h2>Mission Statement</h2>
            <p>At Youth for Seetpur, our mission is to empower, uplift, and transform our community by fostering a culture of education, social responsibility, and environmental stewardship. We are committed to helping students gain access to quality education, supporting social welfare initiatives, and promoting sustainable practices to ensure a clean and healthy environment. Our purpose is to build a well-educated, cohesive, and vibrant Union Council Seetpur where every individual has the opportunity to thrive and contribute to the community's growth and prosperity. Through collaboration, dedication, and innovative solutions, we strive to create a brighter future for all residents of Seetpur.</p>
        </div>
        """,
        unsafe_allow_html=True
    )

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

