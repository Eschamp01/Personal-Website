from . import views
import openai
import os
import pdb

# OpenAI API key defined in .env file, not shared here
openai.api_key = os.environ.get('OPENAI_API_KEY')

# Define a function to make the API call
def generate_text(prompt):
    response = openai.Completion.create(
        engine='text-davinci-003',
        prompt=prompt,
        max_tokens=2000,
        temperature=0.7,
        n=1,
        stop=None,
        timeout=5
    )
    return response.choices[0].text.strip()

def generate_better_text(prompt):
    response = openai.ChatCompletion.create(
    model="gpt-3.5-turbo",
    messages=[
            {"role": "user", "content": prompt}
        ]
    )
    # pdb.set_trace()
    return response.choices[0]['message']['content']

activities_dict = {
    "nature" : "Experiencing the local nature \n",
    "wildlife" : "Seeing the local wildlife \n",
    "local-wines-and-beers" : "Tasting local alcohols, such as wines or beers \n",
    "local-food" : "Trying a selection of local delicacies \n",
    "famous-landmarks" : "Visiting the most famous landmarks in the area \n",
    "beaches" : "Enjoying any local beaches \n",
    "hiking" : "Hiking the most recommended hiking trails in the area \n",
    "watersports" : "Doing popular water sports \n",
}

def construct_prompt(dict):
    prompt = ""

    # Output tone and context, done to optimise the answer quality
    prompt += "Pretend that you are a travel agency, specialised in tailoring vacations to the specific interests of each client. \
            Your job is to provide the best possible suggestions to the client, for them to enjoy their holiday. You do not provide any \
            services for the client. \n \
            A client has given you the following information in order to construct them a detailled holiday plan. The ideal travel \
            itinerary is tailored to the specific needs of the client, but also includes all must-see tourist attractions in the destination. \n"
    
    # The users preferences are given to the Large Language Model in this section
    prompt += "*** \n"
    prompt += f"Construct a travel itinerary for {dict['destination']} from {dict['arrival_date']} to {dict['departure_date']}. \n"
    prompt += f"I arrive at {dict['arrival_time']} on the first day, and leave at {dict['departure_time']} on the final day. \n"
    if dict['relaxed_first_day'] == 'on':
        prompt += "Please provide a travel plan that is more relaxed on the first day of the trip, as I will be tired."
    prompt += f"Overall, the trip should be of a {dict['physical_activity_level']} intensity level."
    if dict["num_travellers"] == 1:
        prompt += f"I will be travelling alone, so please make sure I'm not out alone at night in unsafe areas. \n"
    else:
        prompt += f"I will be travelling in a group of {dict['num_travellers']}, so please make activities suitable for this group size. \n"
    # TODO: Add weather information which is inferred from the travel dates (arrival to departure inclusive)
    prompt += "My interests when travelling are: \n ``` \n"
    for activity in dict["interests"]:
        prompt += activities_dict[activity]
    prompt += "``` \n"
    prompt += "***"

    # Output formatting - done using prompt engineering
    prompt += "Give your response in HTML format. The response should be the part that is contained within the <body> tag of the HTML code. \n \
            Each Day of the trip should be contained within it's own border element. These border elements should have 10 pixels of padding, \
            and a border width of 5 pixels, with a light grey shading and a rounded border. \
            There should be 15 pixels of vertical space between border elements. \n \
            The title of each day should be in a centred h2 tag, and written in the form 'Day [day number] - [main activities] [related emoji]'. \
            This title should be inside of the border element. \n \
            The description of the activities for each day should be between 70 and 150 words. \n \
            Display the Day numbers with h2 tags, and the title each activity highlighted in bold, followed by a short description of the activity. \n"
    
    # Timing precision and how to allocate travel time to/from the airport
    prompt += "Remember to allocate time from the arrival time until 2.5 hours after the arrival time for travel from the airport, and time from \
        2.5 hours before departure time until departure time for travel back to the airport. \n"
    if dict['timing_preciseness'] == "Specific":
        prompt += "Provide the specific time range for when each activity should be done. Each activity heading should be in h4 tags, and be in the form \
            '[activity name] ([start time - end_time])' \
            Timings must be specific for every activity. \
            On days when the client is not travelling to or from the airport, the day should be filled from 9:00 to 20:00."
    else:
        prompt += "Provide rough timings for each activity, splitting the activities up into 'morning', 'afternoon' and 'evening' for each day. \
            Each activity heading should be in h4 tags, and be in the form '[Morning/Afternoon/Evening] - [activity name]'. \n"
    
    # # Include food suggestions inside of the travel plan
    # prompt += "Food suggestions are very important to any tourist's travel experience. For each day, in between the suggested activities, give suggestions \
    #         for meals, with the h4 headings 'Breakfast', 'Lunch', and 'Dinner', followed by a short description of the food, and an address or area to go to to find it. \
    #         Food suggestions should be close to the area that the client is travelling in. \n"
    
    prompt += f"Once again, remember to leave 2.5 hours after the client arrives at {dict['arrival_time']} on {dict['arrival_date']} for travel, and 2.5 \
            hours before they leave at {dict['departure_time']} on {dict['departure_date']}, also for travel."
    
    return prompt


def create_travel_itinerary(dict):
    full_prompt = construct_prompt(dict)
    pdb.set_trace()
    # generate output from engineered prompt
    return generate_better_text(full_prompt)