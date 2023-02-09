import openai
from tabulate import tabulate

def generate_itinerary(input_string):
    # Use the OpenAI API to generate a response to the input string
    response = openai.Completion.create(
        engine="text-davinci-002",
        prompt=input_string,
        max_tokens=1024,
        n=1,
        stop=None,
        temperature=0.5,
        api_key="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"
    ).choices[0].text
    # print(response)

    # Parse the response to extract the itinerary
    itinerary = []
    itinerary.append(["Day", "Activity", "Time", "Comments"])
    lines = response.split("\n")
    day = 1
    for line in lines:
        words = line.split()
        if len(words) != 0:
            if not words[0].isdigit():
                activity = " ".join(words[2:])
                time = words[1]
                comments = ""
                itinerary.append([day, activity, time, comments])
                day += 1
    return itinerary


itinerary = generate_itinerary("I want to plan a trip to " + input("Where are you planning for a trip? ") + " for next weekend. Suggest an itinerary:")

# Print the itinerary
for row in itinerary:
    print(tabulate(itinerary))
