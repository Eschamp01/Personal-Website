# Welcome to TravelGPT

## Contents

[Project Description](#project-description) <br>
[Project Demo](#project-demo) <br>
[Contribute](#contribute)

### Project Description

TravelGPT is a ChatGPT powered assistant which aims to construct the perfect travel itinerary for you. <br>
To plan your ideal holiday, simply fill out the information below, and TravelGPT will do the rest!

This repository is a working progress, with some features still being implemented.


### Project Demo

The website has been deployed using Vercel, and the link is below: <br>
https://travel-gpt-tzrd.vercel.app/travel_plan/ <br>
The backend is currently either very slow or not functional, this is being worked on currently.

Currently, the front-end interface for the user to specify their vacation parameters looks like this: <br>
<img/travel_gpt_initial_frontend>

When all parameters are filled in, the output, which is the fully constructed travel itinerary, looks similar to this: <br>
<img/travel_gpt_initial_itinerary>


### Contribute

To clone this repository, use `git clone`, and access the OpenAI API here: https://openai.com/blog/openai-api <br>

After logging in, you can obtain your secret key. Create a `.env` file in the repository root directory, and populate it with: <br>
`OPENAI_API_KEY = 'YOURKEY'`<br>
You would replace `'YOURKEY'` with the secret key which you obtain from teh OpenAI API website.
