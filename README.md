# Welcome to TravelGPT

## Contents

[Project Description](#project-description) <br>
[Project Demo](#project-demo) <br>
[Testing and Contributing](#testing-and-contributing)

### Project Description

TravelGPT is a ChatGPT powered assistant which aims to construct the perfect travel itinerary for you. <br>
To plan your ideal holiday, simply fill out the information below, and TravelGPT will do the rest!

This repository is a working progress, with features still being implemented. Follow along!


### Project Demo

The website has been deployed using Vercel, and you can [interact with the user interface here](https://travel-gpt-tzrd.vercel.app/travel_plan/). <br>
Currently, the request takes too long for the Vercel free plan, so the "Submit" button doesn't do anything. <br>
To test the program, it is recommended to clone the repo, following the instructions in [Testing and Contributing](#testing-and-contributing)

Currently, the front-end interface, allowing the user to specify their vacation parameters, looks like this: <br>
![travel_gpt_initial_frontend](./img/travel_gpt_initial_frontend.jpg)

When all parameters are filled in, you are redirected to a page which looks similar to this: <br>
![travel_gpt_initial_itinerary](./img/travel_gpt_initial_itinerary.jpg)


### Testing and Contributing

1. Navigate to the folder where you would like to store the project, with `cd <your/desired/folder_path>`.
2. Type `git clone https://github.com/Eschamp01/TravelGPT.git` into the command line.
3. Navigate to the [OpenAI API website](https://openai.com/blog/openai-api), log in, then [generate your API key](https://platform.openai.com/account/api-keys).
4. Create a '.env' file, with `touch .env`, and inside of this file insert the line `OPENAI_API_KEY = 'YOURKEY'`, replacing `'YOURKEY'` with the secret key which you obtain from teh OpenAI API website.
5. Install requirements with `pip install -r requirements.txt`. You may choose to do this in a virtual environment which you have created.
6. Start the application by hosting a local server: run `python manage.py runserver` in the command line.
7. Open your browser of choice, and navigate to the URL `http://localhost:8000/travel_plan/`. Fill in some information about your holiday, and press "Submit". Your travel itinerary will be generated for you shortly!
