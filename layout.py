# streamlit run .\pythonname.py
import streamlit as st

def main():
    st.set_page_config(layout="wide",page_title="CO2 Decarbonization through Supply Chain Optimization",page_icon="📈",)
    st.markdown("<h1 style='text-align: center;'>CO2 Decarbonization through Supply Chain Optimization</h1>", unsafe_allow_html=True)

    desc, input_, output_ = st.tabs(["Description", "Input", "Output"])
    css = """
        <style>
        input[type="number"] {
            text-align: center;
        }
        </style>
        """
        # Render the custom CSS
    st.markdown(css, unsafe_allow_html=True)

    # with st.sidebar:
    #     st.markdown("<h2 style='text-align: center;'> <strong>Input<strong> </h2>", unsafe_allow_html=True)
        
    with desc:
        st.markdown("<h2 style='text-align: center;'>Functionality Description 📜</h2>", unsafe_allow_html=True)
        st.markdown("""<h4 style='text-align: justify;'>Mixed Linear Integer Optimization Algorithm.</h4>""", unsafe_allow_html=True)
        st.markdown("""
        <ul>
        <li style="font-size: 20px;"><strong>Input<strong>: Initial Demands, Growths, Yield, CO2 Emissions, Total Annualised Cost, Maximum Capacity, CO2 Target</li>
        <li style="font-size: 20px;"><strong>Output<strong>: Number of installed technologies, Total TAC, Total CO2 </li>
        <li style="font-size: 20px;"><strong>Objective Functions<strong>: Minimize Total Annualized Cost</li>
        <li style="font-size: 20px;"><strong>Decision Variable: <strong>: Number of installed technologies</li>
        <li style="font-size: 20px;"><strong>Constraints: <strong>
                    <ul>
                    <li style="font-size: 20px;">CO2 Target Fulfillment</li>
                    <li style="font-size: 20px;">Maximum Installed Capacity</li>
                    <li style="font-size: 20px;">Supply Meeting Demand</li>
                    </ul>
                    </li>                            
        </ul>
                    
        """, unsafe_allow_html=True)
        st.markdown("""
            <blockquote style="font-size: 18px;">
                <i>User will need to manually select the relevant predicted figures.</i>
            </blockquote>
            """, unsafe_allow_html=True)

    with input_:
        st.markdown("<h2 style='text-align: center;'>Input Parameters 📥</h2>", unsafe_allow_html=True)
        st.file_uploader("Upload an image to be segmented", type=["png", "jpeg", "jpg"], key = "img_raw")
        if "img" not in st.session_state:
            st.session_state["img"] = 0
        if "pos_y" not in st.session_state:
            st.session_state["pos_y"] = 0
        if "pos_x" not in st.session_state:
            st.session_state["pos_x"] = 0
        if st.session_state["img_raw"] is None:
            st.session_state["width_"] = 100
            st.session_state["height_"] = 100
            with st.spinner("Running 'read_img'"):
                st.session_state["veryimg"] = read_img("image1.png")
                st.success("Running 'read_img'")
            
        elif st.session_state["img_raw"] is not None:
            
            with st.spinner("Running 'read_img'"):
                st.session_state["img"] = read_img(st.session_state["img_raw"])
                st.success("Running 'read_img'")
            st.session_state["width_"], st.session_state["height_"] = st.session_state["img"].size
            st.session_state["img"] = np.array(st.session_state["img"])
            with st.spinner("Running 'plot_on_image'"):
                st.session_state["figure_to_plot"] = plot_on_image(st.session_state["img_raw"], st.session_state["width_"], st.session_state["height_"])
                st.success("Running 'plot_on_image'")
            with st.spinner("unning 'adding slider position'"):
                st.session_state["figure_to_plot"].add_vline(
                x = st.session_state["pos_x"], line_width = 5, line_dash = "dash", 
                line_color = "pink"
                )
                st.session_state["figure_to_plot"].add_hline(
                    y = st.session_state["pos_y"], line_width = 5, line_dash = "dash", 
                    line_color = "red"
                )
                st.success("Running 'adding slider position'")
            with st.sidebar:
                with st.spinner("Plotting the sliders"):
                    x_slide_1, x_slide_2 = st.columns([3, 7])
                    x_slide_1.markdown("<p style='text-align: center;'> x-position: </p>", unsafe_allow_html=True)
                    x_slide_2.slider("x-position", 0, st.session_state["width_"], 30, key = "pos_x", label_visibility = "collapsed")
                    y_slide_1, y_slide_2 = st.columns([3, 7])
                    y_slide_1.markdown("<p style='text-align: center;'> y-position: </p>", unsafe_allow_html=True)
                    y_slide_2.slider("y-position", 0, st.session_state["height_"], 30, key = "pos_y", label_visibility = "collapsed")
                    st.success("Plotting the sliders")
            with st.spinner("Plotting the figures"):
                place = st.empty()
                with place.container():
                    st.plotly_chart(st.session_state["figure_to_plot"], use_container_width=True)
                st.success("Plotting the figures")
                
        if st.button("Run Prediction"):
            predict(st.session_state["img"])

    with output_:
        st.markdown("<h2 style='text-align: center;'>Output Result 📝</h2>", unsafe_allow_html=True)
        
if __name__ == "__main__":
    main()
