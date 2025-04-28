import streamlit as st
import base64

# Page config
st.set_page_config(page_title="My Projects", layout="wide")

# Set background
page_bg_img = '''
<style>
body {
background-image: url("https://images.unsplash.com/photo-1507525428034-b723cf961d3e");
background-size: cover;
background-attachment: fixed;
}
</style>
'''
st.markdown(page_bg_img, unsafe_allow_html=True)

# Center Everything
centered_text = '''
<style>
h1, h2, h3, h4, p, img {
    text-align: center;
    display: block;
    margin-left: auto;
    margin-right: auto;
}
</style>
'''
st.markdown(centered_text, unsafe_allow_html=True)

# Hover Zoom CSS
hover_zoom_css = '''
<style>
.img-hover-zoom img {
    border: 3px solid transparent;
    border-radius: 15px;
    transition: transform 0.4s ease-in-out, 
                border-color 0.4s ease-in-out, 
                box-shadow 0.4s ease-in-out;
    display: block;
    margin-left: auto;
    margin-right: auto;
}
.img-hover-zoom img:hover {
    transform: scale(1.1);
    border-color: #00FFFF;
    box-shadow: 0 8px 20px rgba(0, 255, 255, 0.6);
}
</style>
'''
st.markdown(hover_zoom_css, unsafe_allow_html=True)

# ---- Sidebar ----
st.sidebar.title(" Select A Project")

project_option = st.sidebar.selectbox(
    " ",
    ("Select", "Project 1: Car Price Prediction", "Project 2 : Whatsapp Chat Analyzer", "Project 3 : PowerBi Project")
)

# --------- Main Content
#st.title("📚 Project Description Page")
#st.subheader(" ")

# ---- Project 1 ----
if project_option == "Project 1: Car Price Prediction":
    st.header("🚀 Project 1: Car Price Prediction Model")
    st.markdown("<br>", unsafe_allow_html=True)

    st.markdown("""
            <div style="text-align: center;">
                <ul style="text-align: left; list-style-position: inside;">
                    <li>Achieved <b>92% accuracy</b>. Built using <b>KNN</b> in <b>Python</b>,<b>Streamlit</b> & <b>Streamlit</b>.</li>
                    <li>Simple, user-friendly and uses multiple indicators </b> for easy car price estimation.</li>
                </ul>
            </div>
            """, unsafe_allow_html=True)


    # Function to convert local image to base64
    def get_base64_of_bin_file(bin_file):
        with open(bin_file, 'rb') as f:
            data = f.read()
        return base64.b64encode(data).decode()

    # Your image file
    image_path = "carprice_1.jpg"  # Your local image file name

    img_base64 = get_base64_of_bin_file(image_path)

    # Embed image with hover effect
    st.markdown(f'''
    <div class="img-hover-zoom">
        <img src="data:image/png;base64,{img_base64}" width="800">
    </div>
    ''', unsafe_allow_html=True)

    # Project link
    st.markdown("[🔗 View Project Here](https://carpriceprediction-ses5hg6u2ygattzvcefrnk.streamlit.app/)")
    st.markdown("[🔗 GitHub](https://github.com/Suv1999/car_price_prediction)")


# ---- Project 2 ----
elif project_option == "Project 2 : Whatsapp Chat Analyzer":
    st.header("🚀 Project : Whatsapp Chat Analyzer")
    st.markdown("<br>", unsafe_allow_html=True)

    st.markdown("""
<div style="text-align: center;">
    <ul style="text-align: left; list-style-position: inside;">
        <li>Developed a <b>WhatsApp Chat Analyzer</b> using <b>Python</b>, <b>Streamlit</b>, <b>Matplotlib</b>, and <b>WordCloud</b> libraries.</li>
        <li>Implemented features to analyze chat data based on <b>word frequency</b>, <b>user engagement</b>, <b>message counts</b>, and <b>active hours</b>.</li>
        <li>Visualized chat patterns through <b>interactive bar graphs</b>, <b>word clouds</b>, and <b>time-series plots</b> for deeper insights.</li>
        <li>Enabled users to track the <b>most engaging participants</b>, <b>most frequently used words</b>, and <b>peak messaging times</b> across various time spans.</li>
        <li>Built a <b>dynamic and intuitive dashboard</b> with <b>Streamlit</b>, allowing real-time upload and analysis of chat files.</li>
    </ul>
</div>
""", unsafe_allow_html=True)


    # --- Function to convert local image to base64
    def get_base64_of_bin_file(bin_file):
        with open(bin_file, 'rb') as f:
            data = f.read()
        return base64.b64encode(data).decode()

    # --- Image 1
    image_path1 = "whats app 1.jpg"  # Your first local image
    img_base64_1 = get_base64_of_bin_file(image_path1)

    # --- Image 2
    image_path2 = "whats app 2.jpg"  # Your second local image
    img_base64_2 = get_base64_of_bin_file(image_path2)

    # --- Display two images side-by-side
    col1, col2 = st.columns(2)

    with col1:
        st.markdown(f'''
        <div class="img-hover-zoom">
            <img src="data:image/png;base64,{img_base64_1}" width="800">
        </div>
        ''', unsafe_allow_html=True)

    with col2:
        st.markdown(f'''
        <div class="img-hover-zoom">
            <img src="data:image/png;base64,{img_base64_2}" width="800">
        </div>
        ''', unsafe_allow_html=True)

    # --- Project link
    st.markdown("[🔗 View Project Here](https://8hfxvif8vqwyvkpmumyhbg.streamlit.app/)")

    st.markdown("[🔗 GitHub](https://github.com/Suv1999/whatsapp-analysis-)")
    st.markdown("<br>", unsafe_allow_html=True)

    # --- Display a Video
    st.subheader("🎥 Project Demo Video")

    # Option 1: Upload a local video file
    # video_file = open('your_video.mp4', 'rb')
    # video_bytes = video_file.read()
    # st.video(video_bytes)

    # OR Option 2: Embed YouTube video
    #st.video("https://www.youtube.com/watch?v=D0PlQhBsR1o")  # Replace with your YouTube video link
    st.markdown(" Soon to be uploaded", unsafe_allow_html=True)
    

    
# ---- Project 3 ----
elif project_option == "Project 3 : PowerBi Project":
    
    st.header("🚀 Project : PowerBi Project")
    st.markdown("<br>", unsafe_allow_html=True)

    # --- Function to convert local image to base64
    def get_base64_of_bin_file(bin_file):
        with open(bin_file, 'rb') as f:
            data = f.read()
        return base64.b64encode(data).decode()

    # --- Image 1
    image_path1 = "powerbi.jpg"  # Your first local image
    img_base64_1 = get_base64_of_bin_file(image_path1)

    # --- Image 2
    image_path2 = "p_2.jpg"  # Your second local image
    img_base64_2 = get_base64_of_bin_file(image_path2)


    # --- Image 3
    image_path3 = "p_3.jpg"  # Your first local image
    img_base64_3 = get_base64_of_bin_file(image_path3)

    # --- Image 4
    image_path4 = "p_4.jpg"  # Your second local image
    img_base64_4 = get_base64_of_bin_file(image_path4)

    # --- Display two images side-by-side
    col1, col2 = st.columns(2)
    col3, col4 = st.columns(2)

    with col1:
        st.markdown(f'''
        <div class="img-hover-zoom">
            <img src="data:image/png;base64,{img_base64_1}" width="800">
        </div>
        ''', unsafe_allow_html=True)

    with col2:
        st.markdown(f'''
        <div class="img-hover-zoom">
            <img src="data:image/png;base64,{img_base64_2}" width="800">
        </div>
        ''', unsafe_allow_html=True)

    with col3:
        st.markdown(f'''
        <div class="img-hover-zoom">
            <img src="data:image/png;base64,{img_base64_3}" width="800">
        </div>
        ''', unsafe_allow_html=True)

    with col4:
        st.markdown(f'''
        <div class="img-hover-zoom">
            <img src="data:image/png;base64,{img_base64_4}" width="800">
        </div>
        ''', unsafe_allow_html=True)

    # --- Display a Video
    st.subheader("🎥 Project Demo Video")

    # Option 1: Upload a local video file
    # video_file = open('your_video.mp4', 'rb')
    # video_bytes = video_file.read()
    # st.video(video_bytes)

    # OR Option 2: Embed YouTube video
    #st.video("https://www.youtube.com/watch?v=D0PlQhBsR1o")  
    st.markdown(" Soon to be uploaded", unsafe_allow_html=True)

    # --- Project link
    st.markdown("[🔗 View Project Here](https://yourprojectlink.com)")

else:
    st.title("📚 Project Description Page")
    st.write("Please select a project from the sidebar to view its details.")

