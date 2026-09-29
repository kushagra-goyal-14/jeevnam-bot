# Jivanam Chat Systems

I worked on Jivanam along with my team. I worked on chatbot integration, live chat, and WebRTC setup. Adding the files for rasa bot and socketIO here to be in this place.

- [Team project](https://github.com/programmingninjas/Jivanam)
- [My WebRTC repo](https://github.com/kushagra-goyal-14/Jeevnam-WebRTC)

This has the Rasa bot and live chat, with a small app to run them on their own. WebRTC is in the repo above.

## Run

Use Python 3.8 in a virtual environment.

```sh
pip install -r requirements.txt -r health_bot/requirements.txt
cd health_bot
rasa train
rasa run --connector rest
```

In another terminal, use the same environment and run `python app.py` from the root folder. Open http://127.0.0.1:8080.

Not totally tested and a demo of what we built. Check the repo above for full implementaion.
