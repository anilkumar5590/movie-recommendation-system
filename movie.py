import streamlit as st
import pickle
import pandas as pd
import requests
st.set_page_config(layout="wide",
                   page_title="Movie Recommended System",)


def fetch_poster(movieId):
    response = requests.get("https://api.themoviedb.org/3/movie/{}?api_key=YOUR_API_KEY".format(movieId))
    data = response.json()
    
    poster = data.get('poster_path')
    poster_url = f"https://image.tmdb.org/t/p/w500{poster}"
    return poster_url 
#https://image.tmdb.org/t/p/w500/1E5baAaEse26fej7uHcjOgEE2t2.jpg

def recommended_movie_names(movieName):
    movie_index = movie_df[movie_df['title'] == movieName].index[0]
    distances = similarity[movie_index]
    movie_list = sorted(list(enumerate(distances)), reverse=True, key=lambda x: x[1])[1:10]
    movieName = []
    moviePoster = []
    for i in movie_list:
        movieID = movie_df.iloc[i[0]].movie_id
        movieName.append(movie_df.iloc[i[0]].title)
        moviePoster.append(fetch_poster(movieID))
        
    return movieName, moviePoster

#C:\Users\konat\Desktop\Project\Machine Learning\Movie Recommendation System\movie .pkl
movie_dict = pickle.load(open('movie .pkl', 'rb'))
movie_df = pd.DataFrame(movie_dict)

similarity = pickle.load(open('similar .pkl', 'rb'))
st.title('Movie Recommendation System')

userSelected_MovieName = st.selectbox('Select a movie you like or enter the movie name', movie_df['title'].values)

if st.button('Recommend'):
    names, posters = recommended_movie_names(userSelected_MovieName)

    col1, col2, col3= st.columns(3)
    col4,col5,col6=st.columns(3)
    col7,col8,col9=st.columns(3)
    with col1:
        st.text(names[0])
        st.image(posters[0])
    with col2:
        st.text(names[1])
        st.image(posters[1])
    with col3:
        st.text(names[2])
        st.image(posters[2])
    with col4:
        st.text(names[3])
        st.image(posters[3])
    with col5:
        st.text(names[4])
        st.image(posters[4])
    with col6:
        st.text(names[5])
        st.image(posters[5])
    with col7:
        st.text(names[6])
        st.image(posters[6])
    with col8:
        st.text(names[7])
        st.image(posters[7])
    with col9:
        st.text(names[8])
        st.image(posters[8])
   

# Footer content
footer_html = """
<hr>
<div style="bottom: 0;  color: green; text-align: center;">
    <p style="font-weight: bold; ">Developed by Anil Kumar</p>
</div>
"""

# Display the footer using markdown
st.markdown(footer_html, unsafe_allow_html=True)