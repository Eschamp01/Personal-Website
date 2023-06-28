<div align="center">
  <h1> Welcome to Ariadne </h1>
</div>

### Contents (click to jump to a section)

[Project Description](#project-description) <br>
[Project Demo](#project-demo) <br>
[Prompt Engineering Details](#prompt-engineering-details) <br>
[Testing and Contributing](#testing-and-contributing)


### Project Description

Ariadne is a ChatGPT powered assistant which aims to provide concise and concrete solutions to problems. <br>

Ariadne got its name from the character in Greek mythology who enabled Theseus to escape the labyrinth by using a ball of string, after Theseus had slain the Minotaur. In this project, Ariadne enables the Large Language Model to solve any problem by breaking it down into smaller steps which can be followed, in a similar manner to how Theseus followed the string. <br>

In cases where ChatGPT cannot provide an answer, or provides an answer which is much longer than necessary, Ariadne becomes the problem solver of choice. <br>

Note that the backend is currently not deployed, and examples have been provided in an attempt to demonstrate the user experience.

### Project Demo

The website has been deployed using Vercel, and you can interact with the user interface [here](https://edwardschamp.com/ariadne/). <br>
Currently, the request takes too long for the Vercel free plan, so the "Submit" button doesn't do anything. <br> <br>
Examples of the output are given for a [Numerical problem](http://localhost:8000/ariadne/plane), a [Worded problem](http://localhost:8000/ariadne/moon) and a [Mix of both](http://localhost:8000/ariadne/robots)

To test the program, it is recommended to clone the repo, following the instructions in [Testing and Contributing](#testing-and-contributing)

### Prompt Engineering Details

In the current implementation, there are two prompts which are constructed for each problem that the user wants to solve:
- The first prompt instructs the Large Language Models to construct the steps required to successfully obtain a solution to the problem.
- The second prompt instructs the Large Language model to provide an answer to each step, and in doing so, answer the over-arching problem.

Jump to the functions in the code: [Step-by-step breakdown](https://github.com/Eschamp01/TravelGPT/blob/18ee629f64364ffcc338248ce96643584dabbc09/ariadne/openai_api.py#L32C5-L32C5) -> [Give answers forn each step](https://github.com/Eschamp01/TravelGPT/blob/18ee629f64364ffcc338248ce96643584dabbc09/ariadne/openai_api.py#L94C5-L94C5)

The main sections of the **step construction prompt** are as follows:
1. Instructing the model - The model is instructed to construct informative and concise steps, which are easy to follow.
2. Example response - An example of a problem, and a response which the model should give when presented with this problem, is given. This makes this implementation an example of one-shot learning. This serves to show the model exactly what form of answer it should provide.
3. Output formatting - The format of the answer, although it can be inferred from the example, is specified verbally, to ensure that the model will provide a valid output.
4. Main input - The problem which the model will break down into smaller steps is given, inside the delimiters “*** ***”.
5. Context given by user - The way in which the user has specified that the problem should be tackled, was well as any assumptions that the user has provided, are given to the model in delimiters.

The main sections of the **step answering prompt** are as follows:
1. Instructing the model - The model is instructed to construct clear and precise answers, which are not longer then necessary.
2. Example response - An example of the response which the model should give when presented with the steps, and the original problem, is given. This is also one-shot learning.
3. Output formatting - The required output format is again reiterated.
4. Context - The original problem is provided, in the delimiters “*** ***”
5. Main input - The steps which the model must solve are provided, in the delimiters “<<< >>>”

### Next Steps

Currently, a new front-end page is being constructed which will operate in the following way:

1. The user provides the problem, how they wish the problem to be solved, and any assumptions that must be made or known to solve the problem correctly. 
2. Ariadne only constructs the solution steps that it thinks are suitable, using the user input.
3. The user can edit the steps, and choose to recalculate any given step by clicking on it. 
4. Step 4 can be repeated until the user is happy with the steps.
5. Ariadne will now produce answers to the steps by taking each step, and constructing a prompt to calculate the answer. The prompt will include information on the problem, along with the answers to all previous steps. 
6. The user can edit any of the answers which Ariadne has given, and recalculate any answers they choose to by clicking on that answer.
7. This process is repeated until the user is happy with the answers to each step, and the problem is solved.

The goal of the above implementation is to allow Large Language Models to solve absolutely any task, no matter how large or complex, after enough iterations. If the user interface is sufficiently easy to use, this represents a significant step forward for Large Language Models, since there will no longer a task which they will fail to answer correctly, after enough feedback from the user.

### Testing and Contributing

1. Navigate to the folder where you would like to store the project, with `cd <your/desired/folder_path>`.
2. Type `git clone https://github.com/Eschamp01/TravelGPT.git` into the command line.
3. Navigate to the [OpenAI API website](https://openai.com/blog/openai-api), log in, then [generate your API key](https://platform.openai.com/account/api-keys).
4. Create a '.env' file, with `touch .env`, and inside of this file insert the line `OPENAI_API_KEY = 'YOURKEY'`, replacing `'YOURKEY'` with the secret key which you obtain from teh OpenAI API website.
5. Install requirements with `pip install -r requirements.txt`. You may choose to do this in a virtual environment which you have created.
6. Start the application by hosting a local server: run `python manage.py runserver` in the command line.
7. Open your browser of choice, and navigate to the URL `http://localhost:8000/travel_plan/`. Fill in some information about your holiday, and press "Submit". Your travel itinerary will be generated for you shortly!
