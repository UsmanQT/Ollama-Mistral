import json
import requests

# NOTE: ollama must be running for this to work, start the ollama app or run `ollama serve`
model = "mistral:instruct"  # TODO: update this for whatever model you wish to use


def chat(messages):
    context = []
    for msg in messages:
        r = requests.post(
            "http://localhost:11434/api/chat",
            json={"model": model, "messages": context + [msg], "stream": True},
        )
        r.raise_for_status()
        output = ""

        for line in r.iter_lines():
            body = json.loads(line)
            if "error" in body:
                raise Exception(body["error"])
            if body.get("done") is False:
                message = body.get("message", "")
                content = message.get("content", "")
                output += content
                # the response streams one token at a time, print that as we receive it
                print(content, end="", flush=True)

            if body.get("done", False):
                message["content"] = output
                context.append(message)
                print("\n\n")


def main():
    messages = [
        {"role": "user", "content": "Act as a writing professor. You have given a document to be reviewed and commented upon by your students. You collect all the comments made by a student and try to find the general theme of the comments made. The themes are very general and not specific to any document such as references not added, not having more visual information etc. Do you understand your role?"},
        {"role": "user", "content": """Okay. I will start with giving you a list of comments. Your job is to find the general theme from these comments:\n1. 1. I think you can get rid of these words to make the sentence flow a little better. I like your introduction, it is a good transition into what your main focus is. I don’t know if you plan on highlighting your values, but if you do, you can make a connection point with your goals and how they build off of each other . I think too, the lightening talk for today and Tuesday can be used as a reflection because it applies to who you want to be
missed a word here!
I think in your paragraph 1 plan, you have a good outline of how to enhance your claims by connecting it back to communication.
I may break this up into multiple sentences as it is lengthy and is a little difficult to read.
I may add a sentence about what changes you specifically want to see.
I would say to try and add class readings in the paragraphs you already have, like as support for the points you already have. Especially in the third paragraph you can easily use one of the readings from unit 3 I think.
I think your personal example is a good addition. Maybe try to more directly connect it to communication?
I like that this was made clear in the beginning
don't need
you could maybe use and here because it is affecting all three
my partner and I *
wordy, not very clear
I would talk about honesty and charisma maybe as a patient? What do you as a patient expect from provider with these traits?
you could get rid of "too much"
think you need to add a goals section. I know it might be tough as a patient but you could talk about a goal for the healthcare system based off of our readings.
This sentence answers your first question well. Maybe just include a follow-up sentence about how this can relate to communication with healthcare providers.
If you changed this to "socioeconomic background" it would broaden the groups of people you are talking about, both financially and ethnically (since that is something we also discussed this semester).
Very good job being clear with your role in healthcare communication.
It would be nice to see almost a list of your core values.
Expand on this. This is part of explaining your goals
would you say another value you have is change? Is so, unless different, still state all your values.
*role models
as mentioned in the rubric, we should talk about technological shifts and changing audience. To become more effective, expand on this, and you can most likely find an article from class about this
Leaves the idea of a PA and a physician working together and the importance of communication between the two somewhat in the air.
I like how you are connecting it to your future career but maybe try to change the word choice as I feel it is getting a little repetitive.
I think the citations you have already are very good and connect well, there are definitely more from readings you could add.
My favorite part of this writing is how each topic of improvement is discussed and separated into new paragraphs. As the reader I understood the structure of this writing and recognized this is wrapping up the discussion and talk about who that writer wants to be.
Including the guest speakers into your writing also shows that you were able to integrate others' experiences into your writing.
I would recommend to add a brief thought as to how you will approach people of different color and gender to show what you are taking from your sources you brought in.
This is a really good paragraph for this assignment. One thing I would recommend is that you can even cite this as our last lightning talk assignment.
This is a very good outline of your conclusion, clearly lists each of your core values separately.
Overall good writing and nice connections back to personal experiences and sources used.
I don't know how your experience was, or how much you remember, in the hospital, but if there was a special nurse or doctor that you can connect your points to, and maybe include if that pushed you towards medicine, that would be a good touch.
I would explicitly state your goals and values in your introduction. The intro is vague right now, so you want to let your audience know exactly what they will be reading about.
 The use of your experience in the military really helps this draft. It shows why you have arrived at your values and goals.
Although it leads to good idea, I think having "change" as a value is just too broad. Make it more specific. You do specify on certain aspects, such as how women and race play a role, but make sure you specify that in your topic sentence.
this might be a good place to integrate a source! we had that one reading about the things that make doctors hate their computers, and the design flaws with the charting software. this could be integrated with your personal experience, but also lead you into a great segway to talk about potential changes you might want to make in your future career!
i'm not sure if this is your finished introduction or not, but i think it would help the reader if you started off by more clearly stating what your values and goals are and what you future career is, before jumping into what you already have
you might be able to integrate Lia's story from "take as directed" theres a lot of good stuff in there i feel might relate to and support your claims
Becuase this piece is a full reflection, I think it's okay to list out or directly state what the goal is
Think this type of experience is going to be a great way to set up for showing your past supporting your current goals
I can see where you are going, I think you are on the right tract. You are going through what is applicable or is not, and (assuming this is your introduction paragraph) I think you just need to add in a quick sentence or two that directly state the values relating to goals in everything you want to do as a dentist.
This is a great example to use to put emphasis on transparency, but I wonder if it would be more effective later on when the idea of creating a bond with a patient that way has been supported with your explained values, goals, and the class sources.
Great as a goal, perhaps can include examples of how this might be done.
I think if you are mentioning technology in this here, you need a very specific example of how technology can elaborate complex medical ideas to the patient.
This is great to touch on, I think there are a lot of readings where you can find examples. I think this would also be a great point to pull in a lot of personal experience as a patient.
 I think it is really powerful how you included your own experience and how it has impacted your values and who you want to become.
 I really liked how you seamlessly integrated this quote into your reflection.
I am a little confused, is this what you are claiming as your own values or is this part of the intro hook? If this is what you are claiming to value, I think you are supposed to find a more personal value to consider.
This is a powerful story and I like how you connected it to the communication of the workers.
 This is a good mode of communication from the sources. I would try to include personal reasons for why you would want to undertake a task like this, moreso than your desire to benefit other people. What value is driving your desire to help others?
 You mention being on the receiving end of news as patient. Maybe try to give one specific example and point out what you noticed about their communication
 I assume you already know this, but try to add some more readings throughout. In your second to last paragraph you can use a source of how you plan to use health communication to educate people. Like what specific tools did you learn that you will use.
 I think this is a good start. The addition of more, specific values and how they were developed and shaped through experiences and relationships and how the values can be applied to patient- provider communication will strengthen the paper.
 Is self-advocacy a value that you hold? It seems like this is just a topic you talk about since it is not explicitly stated.
 You have a great start by showing the writer where you are, now discuss how you will be better off in the future from what you learned in this class.
 You have a good point in your second paragraph about how patients need to push themselves, I would recommend discussing the patient/provider interactions and explain how this will improve the quality of the healthcare system.
 I liked how you stated this here as you can are able to find quotes from articles from class. Since there is 3 quotes in one paragraph, it would be better for the reader to break that paragraph up
 This is a strong sentence. Maybe break up paragraphs and have this be the first sentence.
 I like how you mentioned this here. I like the personal story that you included. Maybe look for a strong quote from an article or maybe even from your unit 1 paper
Need the author's last name or title of the article when citing the page number
 It can be effective to list more than one value to go off of.
 This is well written and makes your role very clear.
 agreed, this would be a great place to tie in class material. Maybe you could use one of your guest speakers or one of the articles about race and gender. I believe there are parts in these papers that could help make this point.
 I think this would be a great place to talk about your goals here.
 I would maybe elaborate on this sentence. Just to make it clear how you are "disrespecting" the system. I would assume that maybe you're simply not adding to the system. Disrespecting is a strong word but works great if you can back it.
 How? I would briefly mention how you learned this.
 Are these the values that you are going to be discussing, and if so, will you discuss each one separately and then relate them back to your goals? If so, I would recommend focusing on 3 out of the 4 or 5 due to page restraints.
 I would recommend you try to clarify this sentence as it's a little long. This could potentially be done by getting rid of "who shaped them and how they've developed"
 I think that this essay is outlined very nicely, it seems like you're on the right tract for this assignment!
 I think you expressed what you are passionate about greatly in the first paragraph.
 Try going more into depth about this goal. You can try making it this goal its own paragraph so you are not overwhelming the reader.
 Do you plan on talking about creativity twice or is this the beginning of the paragraph you have written below?  If it is the same paragraph I would just be careful to not repeat information.
 Maybe try to incorporate a guest lecture so you are not focusing on two readings only.
 If you have any real-life experiences, you can try adding those to your claims to make them stronger.
 Very clear and concise
 Talk a little more about your passions in the forensic science field before moving on to what you want to change.
 This seems a little broad, what specifically about how health communication works?
 The personal experience section with Dr. Bryant is a good inclusion. However, one thing I would critique is that it is a tad bit too long. Keep the stuff about how personable she was, but there is a bit of fluff here, like filling out papers and the quotes, that do not seem necessary to me.
 You mentioned in the intro how you got a glimpse at the perspective of the healthcare provider. I would love to see how you incorporate this and how it shaped your values and goals.
 Really good story to introduce why you hold those values and a hint at what context of communication you will be explaining.
 Add in direct quotes from our readings
 Add in some direct quotes from our readings
Add any goals you have involving  health communication"""},
        {"role": "user", "content": "Remove any duplicate themes from the output and give exact list of themes"},
    ]

    chat(messages)


if __name__ == "__main__":
    main()
