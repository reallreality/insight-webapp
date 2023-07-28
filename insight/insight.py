#Importing libraries
import streamlit as page
import pandas as pd
import base64
#from PIL import Image

#Local css for 'email me' form styling
def local_css(local_file):

    with open(local_file) as input_file:

        page.markdown(f'<style>{input_file.read()}</style>', unsafe_allow_html=True)

#Local image opening
def open_bg_image(input_image):

    #Using a context manager to open the local image file
    with open(input_image, 'rb') as input_file:

        #Taking the input image data and passing it to base64 'b64encode' function
        encoded_string = base64.b64encode(input_file.read())

        #Now marking down the actual page so the image appears as the background
        page.markdown(
            f'''
            <style>
            .stApp{{
            background-image: url(data:image/{"png"};base64,{encoded_string.decode()});
            background-size: cover
            }}
            </style>
            ''',
            unsafe_allow_html=True
        )

#Configuring page and tab title and favicon
page.set_page_config('IRM Hackathon Mockup', layout='wide')

#Setting web app background with open_bg_image function
open_bg_image('./IRM_background.png')


#Removing streamlit branding from page
local_css('./style.css')


#Url of google spreadsheet
#url='https://docs.google.com/spreadsheets/d/e/2PACX-1vRFZB4-bJs3WhsVuRH_xD8aypDTpjQo7u-B8uKFFohPdBouayf0XPYfIWhbRPd6MFh0aGSANFCgereK/pub?gid=0&single=true&output=csv'
data = pd.read_csv('./insight_data.csv', dtype=str)


#Header creation container
with page.container():

    page.markdown('<link rel="stylesheet" href="https://maxcdn.bootstrapcdn.com/bootstrap/4.0.0/css/bootstrap.min.css" integrity="sha384-Gn5384xqQ1aoWXA+058RXPxPg6fy4IWvTNh0E263XmFcJlSAwiGgFAW/dAiS6JXm" crossorigin="anonymous">', unsafe_allow_html=True)

    page.markdown("""
    <nav class="navbar fixed-top navbar-expand-lg navbar-dark" style="background-color: #3498DB;">
    <a class="navbar-brand" href="https://www.ironmountain.com/?localize=false&utm_source=Google&utm_medium=paid_search&utm_campaign=US_CoreBrand_Brand_Exact&utm_term=iron_mountain&utm_content=&gad=1&gclid=Cj0KCQjw2eilBhCCARIsAG0Pf8s02RRWCKgCCOoUja1M2_4JJ2eCc4swgeqYVVvgVdTU_MbTqPvVGekaAmPzEALw_wcB&gclsrc=aw.ds" target="_blank">
                <img src="https://i.ibb.co/5LmmZb4/Screenshot-2023-07-21-at-12-18-39-PM-removebg-preview.png" alt="Logo" style="height:35px;">
    </a>
    <button class="navbar-toggler" type="button" data-toggle="collapse" data-target="#navbarNav" aria-controls="navbarNav" aria-expanded="false" aria-label="Toggle navigation">
        <span class="navbar-toggler-icon"></span>
    </button>
    <div class="collapse navbar-collapse" id="navbarNav">
        <ul class="navbar-nav">
        <li class="nav-item active">
            <a class="nav-link disabled" href="#">Home <span class="sr-only">(current)</span></a>
        </li>
        <li class="nav-item">
            <a class="nav-link" href="https://www.ironmountain.com/?localize=false&utm_source=Google&utm_medium=paid_search&utm_campaign=US_CoreBrand_Brand_Exact&utm_term=iron_mountain&utm_content=&gad=1&gclid=Cj0KCQjw2eilBhCCARIsAG0Pf8s02RRWCKgCCOoUja1M2_4JJ2eCc4swgeqYVVvgVdTU_MbTqPvVGekaAmPzEALw_wcB&gclsrc=aw.ds" target="_blank">YouTube</a>
        </li>
        <li class="nav-item">
            <a class="nav-link" href="https://www.ironmountain.com/?localize=false&utm_source=Google&utm_medium=paid_search&utm_campaign=US_CoreBrand_Brand_Exact&utm_term=iron_mountain&utm_content=&gad=1&gclid=Cj0KCQjw2eilBhCCARIsAG0Pf8s02RRWCKgCCOoUja1M2_4JJ2eCc4swgeqYVVvgVdTU_MbTqPvVGekaAmPzEALw_wcB&gclsrc=aw.ds" target="_blank">Twitter</a>
        </li>
        </ul>
    </div>
    </nav>
    """, unsafe_allow_html=True)


#Page title container
with page.container():

    #Create html title
    title = ('''<h2 style="background-color:rgba(255, 255, 255, 0.623); border-radius: 14px; border: 4px solid #E6DFCD; padding:12px; color:white; font-size:45px; font-weight:bold;">InSight Product Support</h2>
''')
             
    page.markdown(title, unsafe_allow_html=True)

#Button tiles container
with page.container():

    #Printing space inbetween title and button tiles
    page.write('###')

    #Three button columns
    left_col, cent_col, right_col = page.columns([5.85,6,4.1])

    
    #Account Maintenance Button
    with left_col:

        page.write(f'''<button style="background-color:rgba(255, 255, 255, 0.623); padding:12px; border: 1px solid #000000; border-radius: 4px;">
                            <a href="https://customersupport.ironmountain.com/s/topic/0TO2H000000QRCR/account-maintenance" target="_blank style="text-decoration: none; color:black;">    
                                <img src="https://i.ibb.co/S3XQTM0/Screenshot-2023-07-21-at-8-42-50-PM.png" alt="Button 1" style="width:250px; height:125px;">
                                <br><span style="text-decoration:none; color:black;">Account Maintenance</span>
                            </a>
                        </button>


        ''', unsafe_allow_html=True)


    #Account support button
    with cent_col:

        page.write(f'''<button style="background-color:rgba(255, 255, 255, 0.623); padding:12px; border: 1px solid #000000; border-radius: 4px;">
                            <a href="https://customersupport.ironmountain.com/s/topic/0TO2H000000QRCS/account-support" target="_blank style="text-decoration:none; color:black;">    
                                <img src="https://i.ibb.co/51bkzsz/Screenshot-2023-07-21-at-8-43-04-PM.png" alt="Button 1" style="width:250px; height:125px;">
                                <br><span style="text-decoration: none; color: black;">Account Support</span>
                            </a>
                        </button>


        ''', unsafe_allow_html=True)


    #Billing button
    with right_col:
        page.write(f'''<button style="background-color:rgba(255, 255, 255, 0.623); padding:12px; border: 1px solid #000000; border-radius: 4px;">
                            <a href="https://customersupport.ironmountain.com/s/topic/0TO2H000000QRCT/billing" target="_blank style="text-decoration:none; color:black;">    
                                <img src="https://i.ibb.co/GFyx1yB/Screenshot-2023-07-21-at-8-43-19-PM.png" alt="Button 1" style="width:250px; height:125px;">
                                <br><span style="text-decoration:none; color:black;">Billing</span>
                            </a>
                        </button>


        ''', unsafe_allow_html=True)


#Creating text search
with page.container():

    #Creating space inbetween tiles and text search
    page.write('###')

    search_input = page.text_input(label=" ", value="")

    search_results_title = data['Country'].str.contains(search_input)
    # search_results_phone = data['Cluster Leader'].str.contains(search_input)
    # search_results_name = data['Name'].str.contains(search_input)
    # search_results_age = data['Age'].str.contains(search_input)

    #This filters what gets returned from the google sheet based on if the input matches any of the columns
    search_query = data[search_results_title]


    #Specifying how many 'cards' we want to show the filtered search results in
    cards_per_row = 3

    #Using a decision to see if a search was entered
    if search_input:

        #Using a for loop to iterate through the dataframe
        for row_index, row_data in search_query.reset_index().iterrows():

            #Seeing if three 'cards' have been read from dataframe
            max_row_content = row_index % cards_per_row

            #If 3 'cards' have been read
            if max_row_content == 0:

                #We write a line
                page.write('---')

                #Creating columns
                columns = page.columns(cards_per_row, gap='large')

                #Specifying which column to write data to
                with columns[row_index % cards_per_row]:

                    #'Who am I' title:
                    page.write(f'<h3 style="backgroundColor:rgba(255, 255, 255, 0.623); border-radius:14px; border: 4px solid #302d28; padding:12px; font-size:20px; color:black;">{row_data["Country"].strip()}</h3>', unsafe_allow_html=True)
    

                    #Displaying other relevant information from row
                    page.write(f'''<p style="backgroundColor:#efefedde; border-radius:14px; border: 2px solid #D3D3D3; padding:12px; font-size:15px; color:grey;">
                               <span style="display: block; font-size: 18px; font-weight: bold; color: black;">Leader: {row_data["Cluster Leader"].strip()}</span>
                               <br><span style="display: block; font-size:15px; font-weight:bold; color:black;">Phone Number: </span>{row_data["Phone"].strip()}<br>
                               <br><span style="display: block; font-size:15px; font-weight:bold; color:black;">Email/s: </span>{row_data["Care General Email"].strip()}<br>
                               <br><span style="display:block; font-size:15px; font-weight:bold; color:black;">Hours of Operation: </span>{row_data["Operation Hours"].strip()}</p>    
                    ''', unsafe_allow_html=True)


#Creating footer
with page.container():

    
    page.markdown('<link rel="stylesheet" href="https://maxcdn.bootstrapcdn.com/bootstrap/4.0.0/css/bootstrap.min.css" integrity="sha384-Gn5384xqQ1aoWXA+058RXPxPg6fy4IWvTNh0E263XmFcJlSAwiGgFAW/dAiS6JXm" crossorigin="anonymous">', unsafe_allow_html=True)

    page.markdown("""
    <footer class="footer fixed-bottom text-white" style="background-color: #3498DB;">
    <a class="navbar-brand" href="https://www.ironmountain.com/?localize=false&utm_source=Google&utm_medium=paid_search&utm_campaign=US_CoreBrand_Brand_Exact&utm_term=iron_mountain&utm_content=&gad=1&gclid=Cj0KCQjw2eilBhCCARIsAG0Pf8s02RRWCKgCCOoUja1M2_4JJ2eCc4swgeqYVVvgVdTU_MbTqPvVGekaAmPzEALw_wcB&gclsrc=aw.ds" target="_blank">
                <img src="https://i.ibb.co/5LmmZb4/Screenshot-2023-07-21-at-12-18-39-PM-removebg-preview.png" alt="Logo" style="height:35px;">
    </a>
    </footer>
    """, unsafe_allow_html=True)

# #Chat container
# with page.container():

#     chat_prompt = page.chat_input('Enter something: ')

#     if chat_prompt:

#         page.chat_message('This is your answer')

