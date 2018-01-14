import fresh_tomatoes
import media

# constructor for instances of class movie variables (in order) movie_title,
# movie_storyline, poster_image_url, trailer_youtube_url

# There Will Be Blood: movie title, storyline, poster image and movie trailer
there_will_be_blood = media.Movie(
    "There Will Be Blood",
    "A story of family, religion, hatred, oil and madness, "
    "focusing on a turn-of-the-century prospector "
    "in the early days of the business.",
    "https://upload.wikimedia.org/wikipedia/en/d/da/There_Will_Be_Blood_Poster.jpg", #NOQA
    "https://www.youtube.com/watch?v=FeSLPELpMeM") #NOQA

# Pulp Fiction: movie title, storyline, poster image and movie trailer
pulp_fiction = media.Movie(
    "Pulp Fiction",
    "The lives of two mob hitmen, a boxer, a gangster's wife, "
    "and a pair of diner bandits intertwine in "
    "four tales of violence and redemption.",
    "https://upload.wikimedia.org/wikipedia/en/3/3b/Pulp_Fiction_%281994%29_poster.jpg", #NOQA
    "https://www.youtube.com/watch?v=s7EdQ4FqbhY") #NOQA

# Caddyshack: movie title, storyline, poster image and movie trailer
caddyshack = media.Movie(
    "Caddyshack",
    "An exclusive golf course has to deal with a brash "
    "new member and a destructive dancing gopher.",
    "https://upload.wikimedia.org/wikipedia/en/8/84/Caddyshack_poster.jpg", #NOQA
    "https://www.youtube.com/watch?v=x9Nl39uWEYk") #NOQA

# Superbad: movie title, storyline, poster image and movie trailer
superbad = media.Movie(
    "Superbad",
    "Two co-dependent high school seniors are forced to deal with separation "
    "anxiety after their plan to stage a booze-soaked party goes awry.",
    "https://upload.wikimedia.org/wikipedia/en/8/8b/Superbad_Poster.png", #NOQA
    "https://www.youtube.com/watch?v=4eaZ_48ZYog") #NOQA

# Dark Knight: movie title, storyline, poster image and movie trailer
dark_knight = media.Movie(
    "The Dark Knight",
    "When the menace known as the Joker emerges from his mysterious past, "
    "he wreaks havoc and chaos on the people of Gotham, the Dark Knight must "
    "accept one of the greatest psychological and physical "
    "tests of his ability to fight injustice.",
    "https://upload.wikimedia.org/wikipedia/en/8/8a/Dark_Knight.jpg", #NOQA
    "https://www.youtube.com/watch?v=kmJLuwP3MbY") #NOQA

# Anchorman: movie title, storyline, poster image and movie trailer
anchorman = media.Movie(
    "Anchorman: The Legend of Ron Burgundy",
    "Ron Burgundy is San Diego's top-rated newsman in the male-dominated "
    "broadcasting of the 1970s, but that's all about to change for Ron and "
    "his cronies when an ambitious woman is hired as a new anchor.",
    "https://upload.wikimedia.org/wikipedia/en/6/64/Movie_poster_Anchorman_The_Legend_of_Ron_Burgundy.jpg", #NOQA
    "https://www.youtube.com/watch?v=-T3wnP91OnI") #NOQA

# The Big Lebowski: movie title, storyline, poster image and movie trailer
the_big_lebowski = media.Movie(
    "The Big Lebowski",
    "The Dude, mistaken for a millionaire Lebowski, seeks restitution "
    "for his ruined rug and enlists his bowling buddies to help get it.",
    "https://upload.wikimedia.org/wikipedia/en/3/35/Biglebowskiposter.jpg", #NOQA
    "https://www.youtube.com/watch?v=cd-go0oBF4Y") #NOQA

# Grand Budapest Hotel: movie title, storyline, poster image and movie trailer
grand_budapest_hotel = media.Movie(
    "The Grand Budapest Hotel",
    "The adventures of Gustave H, a legendary concierge at "
    "a famous hotel from the fictional Republic of Zubrowka "
    "between the first and second World Wars, and Zero Moustafa, "
    "the lobby boy who becomes his most trusted friend.",
    "https://upload.wikimedia.org/wikipedia/en/a/a6/The_Grand_Budapest_Hotel_Poster.jpg", #NOQA
    "https://www.youtube.com/watch?v=1Fg5iWmQjwk") #NOQA

# The Big Sick: movie title, storyline, poster image and movie trailer
the_big_sick = media.Movie(
    "The Big Sick",
    "Pakistan-born comedian Kumail Nanjiani and grad student Emily Gardner fall "
    "in love but struggle as their cultures clash. When Emily contracts a "
    "mysterious illness, Kumail finds himself forced to face her feisty parents, "
    "his family's expectations, and his true feelings.",
    "https://upload.wikimedia.org/wikipedia/en/6/69/The_Big_Sick.jpg", #NOQA
    "https://www.youtube.com/watch?v=PJmpSMRQhhs") #NOQA

# Seven: movie title, storyline, poster image and movie trailer
seven = media.Movie(
    "Seven",
    "Two detectives, a rookie and a veteran, hunt a serial killer who uses the "
    "seven deadly sins as his motives.",
    "https://upload.wikimedia.org/wikipedia/en/6/68/Seven_%28movie%29_poster.jpg", #NOQA
    "https://www.youtube.com/watch?v=znmZoVkCjpI") #NOQA

# Silence of the Lambs: movie title, storyline, poster image and movie trailer
silence_of_the_lambs = media.Movie(
    "The Silence of the Lambs",
    "A young F.B.I. cadet must receive the help of an incarcerated and "
    "manipulative cannibal killer to help catch another serial killer, "
    "a madman who skins his victims.",
    "https://upload.wikimedia.org/wikipedia/en/8/86/The_Silence_of_the_Lambs_poster.jpg", #NOQA
    "https://www.youtube.com/watch?v=ZWCAf-xLV2k") #NOQA

# Godfather: movie title, storyline, poster image and movie trailer
godfather = media.Movie(
    "The Godfather",
    "The aging patriarch of an organized crime dynasty transfers control "
    "of his clandestine empire to his reluctant son.",
    "https://upload.wikimedia.org/wikipedia/en/1/1c/Godfather_ver1.jpg", #NOQA
    "https://www.youtube.com/watch?v=sY1S34973zA") #NOQA

# List of movies for fresh_tomatoes file
movies =[there_will_be_blood,
        pulp_fiction,
        caddyshack,
        superbad,
        dark_knight,
        anchorman,
        the_big_lebowski,
        grand_budapest_hotel,
        the_big_sick,
        seven,
        silence_of_the_lambs,
        godfather]

fresh_tomatoes.open_movies_page(movies)
