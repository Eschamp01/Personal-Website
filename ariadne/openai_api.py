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

def construct_steps_prompt(dict, list:bool):
    prompt = ""

    # Output tone and context, done to optimise the answer quality
    prompt += "You are InstructGPT, an expert at giving instructions to break down problems. Whenever you are provided with a problem, you always give detailed instructions to \
break it down into smaller steps.  You make sure that you include all of the needed background information in each instruction. \
To solve the problem, the smaller steps can each be answered in turn. \
You greatly enjoy making others answer your instructions, so you never give the answers, or suggest answers to your instructions. \
The answer to the final instruction that you ask is the final answer to the overall problem. \
You always begin an instruction with a verb. You always end the last instruction with 'This gives your final answer.'"

    prompt += "Your instructions should be specific, but you never give suggestions or answers to your own instructions."
    
    # Example of a response to give, so this is one-shot learning
    if list:
        prompt += 'Here is an example: \
``` \
The following problem is given to you: *** "What is the maximum apples that the average person can eat in a day?" *** \
Your response: ["This is about the food apples, and human eating speeds. Calculate how long it takes for the average person to eat an apple", \
"This is about human chewing speed. Find how long can the average person chew for per day", \
"Divide the time someone can chew for by the time taken to eat an apple. This gives your final answer." \
] \
``` '
        prompt += " Your response must be a valid python list. Strings containing apostrophes or single quotes are enclosed in double quotes. \
Strings containing double quotes are enclosed in single quotes."

    else:
        prompt += "Here is an example: \
``` \
User: 'What is the maximum apples that the average person can eat in a day?' \
Your response: { \
'step 1' : 'How long does it take the average person to eat an apple?', \
'step 2' : 'How long can the average person chew for per day?', \
'step 3' : 'By dividing the time someone can chew for by the time taken to eat an apple, how many apples can the average person eat in a day?', \
} \
``` "
        prompt += " Your response must be a valid dictionary oject."

    prompt += "The following problem is given to you: "
    # The users preferences are given to the Large Language Model in this section
    prompt += "*** "
    prompt += f"{dict['problem']} "
    prompt += "*** "

    # Additional information and hint processing
    prompt += "The user has given the following additional information to help you construct your step-by-step questions: "
    prompt += "''' "
    for assumption in dict['assumptions']:
        prompt += " - " + assumption + " "
    prompt += "''' "

    if dict['method'] is not "":
        prompt += f"You should approach the problem in the following way: \
<<< {dict['method']} >>>"

#     # Output formatting reiterated to ensure correct output
#     prompt += "Give your response in dictionary format, with keys equal to 'step 1', 'step 2', etc, and values equal to the \
# smaller steps which you have broken the problem down into."
    
    return prompt

def construct_answers_prompt(problem_dict, steps, list:bool):
    prompt = ""

    # provide the problem as context
    prompt += f"You are FollowGPT, an instruction follower. You find precise answers to instructions. You will be provided \
with a series of instructions, and your goal is to solve each instruction, giving the answer to it. \
You really like to give specific names, numbers, or facts which answer the instruction. \
When asked to research or provide information, you like to give specific lists of answers. You never repeat the instruction back. \
You avoid repeating words given in the instructions, since you like to be concise. You always answer the master problem with the final instruction answer."

    # Example of a response to give, so this is one-shot learning
    if list:
        prompt += 'Here is an example: \
``` \
Master problem: *** "What is the maximum apples that the average person can eat in a day?" *** \
Instructions: ["Calculate how long it takes for the average person to eat an apple", \
"Find how long can the average person chew for per day", \
"Divide the time someone can chew for by the time taken to eat an apple. This gives your final answer." \
] \
Your response: [ \
"The answer is 5 minutes", \
"12 consecutive hours. This is equal to 720 minutes", \
"720 / 5 = 144 apples. Final answer: the average person can eat 144 apples in a day.", \
] \
``` '
        # Output formatting reiterated to ensure correct output
        prompt += "Give your response as a valid python list."

    else:
        prompt += "Here is an example: \
``` \
Prompt: { \
'step 1' : 'How long does it take the average person to eat an apple?', \
'step 2' : 'How long can the average person chew for per day?', \
'step 3' : 'By dividing the time someone can chew for by the time taken to eat an apple, how many apples can the average person eat in a day?', \
} \
Your response: { \
'step 1' : 'It takes the average person 5 minutes to eat an apple.', \
'step 2' : 'The average person can chew for 12 consecutive hours per day. This is equal to 720 minutes', \
'step 3' : '720 / 5 = 144 apples. The average person can eat 144 apples in a day.', \
} \
``` "
        # Output formatting reiterated to ensure correct output
        prompt += "Give your response as a valid python dictionary. "
    
    # Smaller steps to answer

    prompt += "Now, for your real task! "
    prompt += f"Master problem: *** {problem_dict['problem']} ***"
    prompt += "Instructions: "

    if list:
        prompt += "''' ["
        for step in steps:
            prompt += '"' + step + '"' + ", "
        prompt += "] '''"
        
    else:
        prompt += "''' {"
        for step_num, step in steps.items():
            prompt += step_num + " : " + step + ", "
        prompt += "} '''"

    prompt += "Make sure to answer each instruction with the most precise and concise answer possible."

    # Additional information and hint processing
    # prompt += "The following additional information may be useful: "
    # prompt += "''' "
    # for assumption in problem_dict['assumptions']:
    #     prompt += " - " + assumption + " "
    # prompt += "''' "

    return prompt


def break_down_problem(dict, list):
    full_prompt = construct_steps_prompt(dict, list)
    return generate_better_text(full_prompt)

def get_answers(problem_dict, steps, list):
    answers_prompt = construct_answers_prompt(problem_dict, steps, list)
    return generate_better_text(answers_prompt)