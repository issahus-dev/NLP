import spacy
nlp = spacy.load('en_core_web_md')

film = {'planet Hulk':'Will he save their world or destroy it? When the Hulk becomes too dangerous for the Earth, the Illuminati trick Hulk into a shuttle and launch him into space to a planet sakaar where he is sold into slavery and trained as a gladiator.'}

#reading txt file, and storing the movie and description in a dict.
with open('movies.txt', 'r') as f:
    data = f.readlines()
    movies = {}
    for item in data:
        split_data = item.split(':')
        movies[split_data[0]] = split_data[1].replace('\n',"")



        
def recomendation(desc):
    recommends = {}
    rating = []
    token_ = nlp(desc)    
    for key, value in movies.items():
        token = nlp(value)
        sim = token_.similarity(token)
        rating.append(sim)
        recommends[key] = sim
    
    for key, value in recommends.items():
        if max(rating) == value:
            return key

print(recomendation('Will he save their world or destroy it? When the Hulk becomes too dangerous for the Earth, the Illuminati trick Hulk into a shuttle and launch him into space to a planet sakaar where he is sold into slavery and trained as a gladiator.'))
     

#plan for when i comeback, create a dict containing the movie hulk, iterate over both dict, store score value as an int
# while iterating through the dicts, create another dict containing a key of films and similarty score. and return the key of
#the film which has the highest score.