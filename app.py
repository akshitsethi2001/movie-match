import pickle
import streamlit as st
import requests

def fetch_poster(movie_id):
    url = "https://api.themoviedb.org/3/movie/{}?api_key=9062682b2658292d1e661e8a80ace4fe&language=en-US".format(movie_id)
    data = requests.get(url)
    data = data.json()
    poster_path = data['poster_path']
    full_path = "https://image.tmdb.org/t/p/w500/" + poster_path
    return full_path

def recommend(movie):
    index = movies[movies['title'] == movie].index[0]
    distances = sorted(list(enumerate(similarity[index])), reverse=True, key=lambda x: x[1])
    recommended_movie_names = []
    recommended_movie_posters = []
    for i in distances[1:6]:
        movie_id = movies.iloc[i[0]].movie_id
        recommended_movie_posters.append(fetch_poster(movie_id))
        recommended_movie_names.append(movies.iloc[i[0]].title)
    recommended_movie_ids = [movies.iloc[i[0]].movie_id for i in distances[1:6]]
    return recommended_movie_names, recommended_movie_posters, recommended_movie_ids

st.header(':red[Movie Match]')
st.markdown(""" Your Personal Movie Recommender """)
movies = pickle.load(open('movie_list.pkl', 'rb'))
similarity = pickle.load(open('similarity.pkl', 'rb'))

# CSS styles
st.markdown(
    """
    <style>
    .poster-container {
        position: relative;
        display: inline-block;
    }

    .poster-image {
        width: 120px;
    }

    .line {
        position: absolute;
        bottom: -10px;
        left: 0;
        width: 100%;
        height: 2px;
        background-color: red;
        visibility: hidden;
        transform: translateX( 0%);
        transition: visibility 0s linear 0.1s, transform 0.1s;
    }

    .poster-container:hover .line {
        visibility: visible;
        transform: translateX(0);
    }
    </style>
    """,
    unsafe_allow_html=True
)

movie_list = movies['title'].values
selected_movie = st.selectbox(
    "Type or select a movie from the dropdown",
    movie_list
)

if st.button('Show Recommendation'):
    recommended_movie_names, recommended_movie_posters, recommended_movie_ids = recommend(selected_movie)
    col1, col2, col3, col4, col5 = st.columns(5)
    with col1:
        st.text(recommended_movie_names[0])
        st.markdown(
            f"""
            <div class='poster-container'>
                <a href='https://www.themoviedb.org/movie/{recommended_movie_ids[0]}' target='_blank'>
                    <img src='{recommended_movie_posters[0]}' alt='Poster' class='poster-image'>
                    <div class='line'></div>
                </a>
            </div>
            """,
            unsafe_allow_html=True
        )

    # Repeat the same pattern for the other columns
    with col2:
        st.text(recommended_movie_names[1])
        st.markdown(
            f"""
            <div class='poster-container'>
                <a href='https://www.themoviedb.org/movie/{recommended_movie_ids[1]}' target='_blank'>
                    <img src='{recommended_movie_posters[1]}' alt='Poster' class='poster-image'>
                    <div class='line'></div>
                </a>
            </div>
            """,
            unsafe_allow_html=True
        )

    with col3:
        st.text(recommended_movie_names[2])
        st.markdown(
            f"""
            <div class='poster-container'>
                <a href='https://www.themoviedb.org/movie/{recommended_movie_ids[2]}' target='_blank'>
                    <img src='{recommended_movie_posters[2]}' alt='Poster' class='poster-image'>
                    <div class='line'></div>
                </a>
            </div>
            """,
            unsafe_allow_html=True
        )

    with col4:
        st.text(recommended_movie_names[3])
        st.markdown(
            f"""
            <div class='poster-container'>
                <a href='https://www.themoviedb.org/movie/{recommended_movie_ids[3]}' target='_blank'>
                    <img src='{recommended_movie_posters[3]}' alt='Poster' class='poster-image'>
                    <div class='line'></div>
                </a>
            </div>
            """,
            unsafe_allow_html=True
        )

    with col5:
        st.text(recommended_movie_names[4])
        st.markdown(
            f"""
            <div class='poster-container'>
                <a href='https://www.themoviedb.org/movie/{recommended_movie_ids[4]}' target='_blank'>
                    <img src='{recommended_movie_posters[4]}' alt='Poster' class='poster-image'>
                    <div class='line'></div>
                </a>
            </div>
            """,
            unsafe_allow_html=True
        )
