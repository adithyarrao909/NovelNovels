# sysdefs.py - Define constants or system-wide configurations

TOP_RATED = "10"
# GoogleBooks API key
GBOOKS_API_KEY = "AIzaSyAoqVPohqCXnWYcRGhe2sA_Ygyd4JPS1So"

class Books_c:
    def __init__(self, title="No Title", author="No Author", release_year = "No Release Year", url = "No URL", json=None, similarity = 0):
        self.json = json
        self.title = title
        self.author = author
        self.release_year = release_year
        self.url = url
        self.similarity = similarity
        if json:
            self.json_parser()

    def info(self):
        return (self.title + " by " + self.author + " (" + str(self.release_year) + ")")  # Concatenate
    
    def json_parser(self):
        print(self)
        for i,book in enumerate(self):
            if(book[i] == 'title'):  # Made to match sample_json. Will need trackName for intended use. 
                self.title = self.json[i]
            if(i == 'author_name'):
                self.author = self.json[i]
            if(i == 'ratings_average'):
                self.rating_avg = self.json[i][0:4]