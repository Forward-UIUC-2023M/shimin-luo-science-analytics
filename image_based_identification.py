from serpapi import GoogleSearch
import requests
from deepface import DeepFace

def search(name):
    params = {
      "engine": "google",
      "q": name,
      "location": "Austin, Texas, United States",
      "google_domain": "google.com",
      "gl": "us",
      "hl": "en",
      "api_key": "602c89e563bc7409332950937424688cccdfe8fd7671c9f46fd2fa507c4bfb13"
    }

    search = GoogleSearch(params)
    results = search.get_dict()
    print(results)
    print(results['organic_results'][0])
    print(results['organic_results'][0]['thumbnail'])

    url = results['organic_results'][0]['thumbnail']
    return url

def load_image(filename, url):
    response = requests.get(url)

    if response.status_code == 200:
        with open(filename, "wb") as f:
            f.write(response.content)
        print("Image downloaded successfully as", filename)
    else:
        print("Failed to download the image.")

if __name__ == "__main__":
    filename = "grasp_image.jpg"
    url = search("Agouris,Peggy")
    load_image(filename, url)
    obj = DeepFace.analyze(filename, actions = ["age", "gender", "race"])
    print(obj)
    print("dominant_gender: " + obj[0]['dominant_gender'])
    print("dominant_race: " + obj[0]['dominant_race'])
