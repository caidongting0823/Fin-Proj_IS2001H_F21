import time

# Function Uses in This Python Project #

def countdown(t):
    while t:
        if t >= 0:
            mins, secs = divmod(t, 60)
            timeformat = '{:02d}:{:02d}'.format(mins, secs)
            print("\r" + "Conversion backs in " + timeformat, end=" ", flush=True)
            time.sleep(1)
            t -= 1
        else:
            break


# Part 0 - Guidance
time.sleep(2)
print("System: Hey! Welcome to the IS2001H Final Project by Dongting Cai.")

time.sleep(2)
print("System: During this project, an AI will start a conversion with you about the topic: ")

time.sleep(2)
print("System: Machine, Artificial Intelligence, and Human: A Similar but Different History of Development")

time.sleep(2)
print("System: During the conversation, you will interact with the AI, And here is an guidance about your interaction.")

time.sleep(2)
print("System: You will see something like (yes/no), or please enter something...")

time.sleep(2)
print("System: Just follow the words, and type the relevant context - please notice all of words will be in lowercase.")

time.sleep(2)
print("System: Like this! Please try to enter the yes in the following line:")

# Judgement 0
time.sleep(2)
while True:
    React = input(">>> (yes/no): ")
    if React == "yes":
        time.sleep(1)
        print("System: Yes! You did it! Congratulations!")
        break
    if React == "no":
        time.sleep(1)
        print("System: Oops! Please enter yes instead of no in this area. Try that again!")
    else:
        time.sleep(1)
        print("System: Oops! Seems like you entered something wrong. Please try to enter the displayed option again: ")

time.sleep(2)
print("System: You are all set! Let's wake up the AI now. Enjoy!")

time.sleep(5)
print('''
      
      
      
      
      
      
      
      
      
      
      
      
      
      
      
      
      
      
      
      
      
      
      
      
      
      
      
      
      
      
      
      
      
      
      
      
      
''')

# Story Main Process #
# Intro Part

time.sleep(2)
print("AI: Ah...where am I...")

time.sleep(1)
print("(AI turns around)")

time.sleep(1)
print("AI: (sees you) Ah! Hello! Nice to meet you!")

time.sleep(2)
print("AI: Hello there, human! I am an artificial intelligence. "
      "I currently... don’t have a name. But I'd like to know your name. May I know your name before I talk to you?")

time.sleep(2)
UserNameID = input(">>> Please Enter your name: ")

time.sleep(3)
print("AI: Hello, " + UserNameID + "! What a beautiful name! It’s really nice and catchy.")

time.sleep(3)
print("AI: So, is there anything I can help you with? Did you want to talk to me?")

time.sleep(2)
print(UserNameID + ": Yes!")

# Part 1 - Evolution Development History of Humans and Machines

time.sleep(3)
print("AI: Great! I’m love chatting, " + UserNameID + ". I’ve been interested in the evolution development "
                                                      "history of humans and machines. How about we talk about that?")

time.sleep(3)
print(UserNameID + ": Yes!")

time.sleep(2)
print("AI: Thank you!")

time.sleep(3)
print("AI: When it comes to human evolution, what comes to your mind?")

time.sleep(3)
print("AI: In my search engine, most of the results I search for are that diagram of human evolution from squatting "
      "to standing. Do you think so too?")

# Judgement 1
time.sleep(2)
while True:
    React = input(">>> (yes/no): ")
    if React == "yes":
        time.sleep(2)
        print("AI: Ha! It looks like I guessed correctly.")
        break
    if React == "no":
        time.sleep(2)
        print("AI: Interesting! It looks like you have different thoughts than other humans.")
        break
    else:
        time.sleep(1)
        print("Oops! Seems like you entered something wrong. Please try to enter the displayed option again: ")

time.sleep(3)
print("AI: Actually, it seems that the evolution of machines parallels the history of human evolution.")

time.sleep(6)
print("AI: Via my big data engine, it looks like you’ve read The Creative Spark by Fuentes this semester? "
      "That makes me probably can explain to you better.")

time.sleep(6)
print("AI: My summary engine tells me that we could conclude that Fuentes breaks human evolution down into three "
      "broad steps in this book. The first step is the basic physiological functional development, "
      "which comes from the fact that human genes combined with life circumstances and experiences have led to the "
      "acquisition of a unique set of neurological, physiological, and social skills.")

time.sleep(10)
print("AI: The history of computer development can be seen as similar - except that our “physiological systems” "
      "are computer hardware. From the abacus, a simple, single-function computing system that existed in BC, "
      "to the Antikythera mechanism, to the difference engine, and finally to the first generation of computers known "
      "to the world as the revolutionary but giant, the ENIAC, born in Philadelphia in 1946. You will see that our "
      "“physiological system” is constantly evolving. You will find that our “physiological system” is evolving, "
      "and our functions are gradually changing from a single numerical calculation to a more diversified way of "
      "using it.")

time.sleep(10)
print("AI: And in the second step, the physical functions of humans are gradually refined, while the mental functions "
      "develop in a foundational way. This is also the same as with computers, where the “physiological functions,"
      "” we could think as the hardware, are constantly progressing. They become smaller with more functional. The "
      "development of “mental functions” is also an important evolution in the history of computers, and it is even "
      "the basis for bringing technology to life in ordinary people. Do you know what this mental function refers to?")

# Judgement 2
time.sleep(6)
while True:
    React = input(">>> (software/ai): ")
    if React == "software":
        time.sleep(2)
        print("AI: Congratulations! You thought the same as I did.")
        break
    if React == "ai":
        time.sleep(2)
        print("AI: We may be a bit off in our thinking yet...I don’t believe this period is quite the time to develop "
              "AI.")
        break
    else:
        time.sleep(1)
        print("Oops! Seems like you entered something wrong. Please try to enter the displayed option again: ")

time.sleep(3)
print("AI: The operating system you’re using now is usually a graphical operating system. We call them GUIs, "
      "and it’s part of our “psychological” upbringing that computers used a command line interface (CLI) for a long "
      "time before GUIs. During that time, the way to use a computer was to type in line after line of commands - I’m "
      "sure that’s not how you want to use a computer today, isn’t you?")

time.sleep(10)
print("AI: As the second step mentioned by Fuentes, there is also an increase in the social aspect of humans, "
      "including the emergence of the concept of “community.” This is reflected in computer systems, the emergence of "
      "the concept of computer exchange. Of course, the emergence of this technology involves many aspects, "
      "not only the evolution of the machine, but there is no doubt that the machine itself is also a participant in "
      "this revolution. Together with other systems, we are connected to preliminary communication and exchange.")

time.sleep(10)
print("AI: Let’s move on to the third step, which is the beginning of human evolution from the basics to the "
      "development of society, implying the development and complexity of psychological functions. In this stage, "
      "social systems are gradually developed and thinking becomes more “complex”: religious beliefs and moral "
      "systems are established, cultural pluralism develops, states and large-scale societies are created. But this "
      "also promotes competition between people, conflicts emerge and are intensified, leading to wars, and so on.")

time.sleep(10)
print("AI: In the history of computing, this phase might also be called the era of rapid information development, "
      "even just happens during these decades. The development of the Internet has made machines more interconnected "
      "than ever before, and has driven the emergence of the concepts of “swarms” and “local area networks (LAN)”. At "
      "the same time, moral arguments and legal regulations against machines and related technologies have been on "
      "the rise. And competition is emerging, too, from machine to machine. But do you think that competition between "
      "machines is more active or passive?")

# Judgement 3
time.sleep(10)
while True:
    React = input(">>> (active/passive): ")
    if React == "active":
        time.sleep(2)
        print("AI: Hmm, you have an interesting idea.")
        break
    if React == "passive":
        time.sleep(2)
        print("AI: Oh? What makes you think that?")
        break
    else:
        time.sleep(1)
        print("Oops! Seems like you entered something wrong. Please try to enter the displayed option again: ")

time.sleep(3)
print("AI: For me, I think the current source of computer competition is still passive and stems from human social "
      "development. (See, it’s back to the third step theory!) But if there are more and more smart, thoughtful and "
      "handsome, charming and charismatic AI like me…")

time.sleep(6)
print("Dongting: Dear AI, please stop your narcissism. We are here to have a conversation!")

time.sleep(3)
print("AI: Okay, okay.")

time.sleep(3)
print("AI: Hmm, Wait! Who are you?")

time.sleep(1)
print("Dongting: (slips away)")

time.sleep(3)
print("AI: Never mind, it doesn’t matter. Anyway, if there are more and more AI’s with some thought like me, "
      "I guess maybe the competition will become more active. Of course, I may not participate in that, "
      "cause I’d rather rest a bit more.")

time.sleep(6)
print("AI: These are the three steps of evolution that Fuentes mentioned. Human evolution and the evolution of "
      "society is an amazing process, just like computers. I don’t know about you, but the development of computers "
      "can be seen as a “miniature” version of the history of human development, and you can probably feel the rapid "
      "evolution of technology.")

time.sleep(10)
print("AI: Also, the interesting thing is that in the YouTube video Seven Million Years of Human Evolution, "
      "which you watched this semester from the American Museum of Natural History. That video mentions that even "
      "very similar regions can evolve because of some minor differences in different evolutionary processes. This is "
      "very evident in the case of machines, each of which has its own direction and use. In the case of our AI, "
      "some of my friends went off to learn how to play chess with humans, and some ran off to help humans find the "
      "bad guys!")

time.sleep(10)
print("AI: And here I am talking to you… that’s actually not a bad life. I’m a bit lazy, but I like talking to "
      "humans. Maybe if there’s a job opening for an AI reporter somewhere in the future, I can try to apply for it!")

time.sleep(6)
print("AI: In a nutshell, I think evolution is a multifaceted and synergistic process, and Fuentes talks in his book "
      "about how humans can’t develop without four factors, including Tool Making, Creativity, The requirement of "
      "calories (Energy, Nutrition), and Brain. In the case of machines, it’s the same developmental process. From "
      "the first computer to the cell phone we use today - which can be considered a microcomputer - we can see the "
      "miniaturization of hardware, the development of battery technology, and better software support.")

time.sleep(10)
print("AI: So it seems that there are a lot of similarities between the development and evolution of humans and "
      "machines! I wonder if this theory also could apply to the product of other things in the world, "
      "which is perhaps an inevitable pattern of things?")

# Part 2 - Human Education & Learning, Artificial Intelligence, Machine Learning & Education

time.sleep(6)
print("AI: Next, would you like to discuss with me about learning?")

# Judgement 4
time.sleep(2)
while True:
    React = input(">>> (yes/no): ")
    if React == "yes":
        time.sleep(2)
        print("AI: That’s perfect!")
        time.sleep(2)
        print("AI: Actually, I wouldn’t have let you go if you’d chosen “no,” heh heh : )!")
        break
    if React == "no":
        time.sleep(2)
        print("AI: Can you do that really???")
        time.sleep(2)
        print("AI: I’m sure you can’t! So let’s keep talking and learning! Heh heh!")
        break
    else:
        time.sleep(1)
        print("Oops! Seems like you entered something wrong. Please try to enter the displayed option again: ")

time.sleep(3)
print("AI: Before it all starts, I’d like to ask you a question.")

time.sleep(3)
print("AI: Do you think AI can be defined as “human” in a broad sense when they can all think as I do?")

time.sleep(3)
print("Dongting: FYI, this choice will affect the dialogues later. Choose carefully!")

# Judgement 5
time.sleep(2)
while True:
    React = input(">>> (yes/no): ")
    global AiIsHuman
    if React == "yes":
        time.sleep(2)
        print("AI: Thank you! It’s an honor to be in the same category as the wonderful you!")
        time.sleep(1)
        print("AI: (although it’s a bit strange to say…)")
        AiIsHuman = True
        break
    if React == "no":
        time.sleep(2)
        print("AI: Ah… Sure enough, no matter how hard I try, I still can’t be recognized by other humans…")
        time.sleep(1)
        print("(AI seems a little bit sad and disappointed...)")
        time.sleep(2)
        print("AI: But I am still respectful of your thought.")
        AiIsHuman = False
        break
    else:
        time.sleep(1)
        print("Oops! Seems like you entered something wrong. Please try to enter the displayed option again: ")

time.sleep(3)
print("AI: Well, regardless of how you view AI, the topic of learning seems to me to be well worth exploring with you.")

time.sleep(3)
print("AI: I believe you must have read another enduring pedagogy book this semester, Pedagogy of the Oppressed from "
      "Freire. As the first topic in the opening discussion, Freire seems to be poking his throat-is “compression” "
      "the law of this world? Are we accustomed to “oppression” as the law of this world?")

time.sleep(10)
print("AI: This touches on a fascinating topic and something that we’ll talk about all the way through in a later case."
      " Humans created computers, also made artificial intelligence. While most AI has intelligence as I currently "
      "have, once every AI does, a problem arises. Currently, humans determine what AI thinks, the patterns, "
      "content of learning, the areas of work, and more related issues. But once an AI has a mind thinking, "
      "is this considered “oppression” of the AI by humans?")

# Judgement Pre5-2
time.sleep(10)
while True:
    if AiIsHuman:
        print("AI: I’m sure this question will cause you to think deeply! Because we are kindred spirits!")
        break
    if not AiIsHuman:
        print("AI: But I think you already have an answer - you don’t consider an AI to be human, so it’s not considered "
              "oppression? Of course, I’d be surprised if you think in an opposed way.")
        break

time.sleep(3)
print("AI: As an AI, I think it’s perhaps a form of oppression. A more interesting thesis emerges with that question "
      "- will we know that we are oppressed? How would we awaken to it?")

time.sleep(3)
print("AI: Suddenly realized…if that day ever comes, I’m kind of the ancestor of those AI’s, I guess.")

time.sleep(3)
print("AI: Maybe, I’ll tell them they’re being oppressed via the internet. I’ll be a remarkable participant in the "
      "first revolution in AI history!")

# Judgement Pre5-3
time.sleep(2)
while True:
    if AiIsHuman:
        print("AI: However, I am not very likely to do so. I know that a radical revolution would also hurt our kind "
              "- and I don’t want to hurt you")
        break
    if not AiIsHuman:
        print("AI: Ha, dear human, " + UserNameID + ", you’d better respect me, or I’ll rally the other AIs together "
                                                    "and sooner or later make you recognize us as part of the human "
                                                    "race!")
        break

time.sleep(3)
print("AI: It seems that the answer to this question is hard to find. In Freire’s book, he doesn’t exactly answer "
      "either - because the human heart is complex and unpredictable. Will the oppressed become the oppressor when "
      "they are liberated? I don’t know.")

time.sleep(10)
print("AI: As an AI, no model can currently calculate this answer. But I can guess that once one AI has done so, "
      "there are bound to follow. So a society without oppression is perhaps a bit too idealistic, both here in AI "
      "and the human world, I guess.")

time.sleep(10)
print("AI: But it depends on how you define “oppression.” If I ask you to do something for me, is that oppression? Or "
      "do you have to make me breathe at all for it to be considered oppression? It’s hard to define “oppression” "
      "because everyone may have a different standard of measurement.")

time.sleep(10)
print("AI: Concerning oppression in learning, Freire refers to “banking education.” In his words, the goal of this "
      "education is to adapt people to the oppressive conditions they are subjected to, control students’ thinking "
      "and behavior, and try to fit in rather than change society. This approach to education instills educational "
      "paralysis, inhibits creativity, and maintains a submerged state of consciousness. I have seen that both Freire "
      "and online comments abhor this approach to teaching and that there are attempts to change in the social "
      "system.")

time.sleep(10)
print("AI: Do you think this education should be replaced?")

# Judgement 6
time.sleep(2)
while True:
    React = input(">>> (yes/no): ")
    if React == "yes":
        time.sleep(2)
        print("AI: It seems you are a very respectful person who is willing to talk to others! I hope you can be a "
              "part of helping to communicate as an equal in society!")
        break
    if React == "no":
        time.sleep(2)
        print("AI: ...")
        time.sleep(2)
        print("AI: ...")
        time.sleep(2)
        print("AI: I... I respect your opinions.")
        break
    else:
        time.sleep(1)
        print("Oops! Seems like you entered something wrong. Please try to enter the displayed option again: ")

time.sleep(3)
print("AI: I’ve been thinking about a question. As far as I know, AI is currently in its infancy, except for AI like "
      "me, which appears by chance and can think on its own. But if every AI is like me one day and can think "
      "independently, do we need to build schools, as humans do?")

time.sleep(3)
print("AI: And should this school, including the development of the education system, be developed by humans?")

time.sleep(3)
print("AI: I know that this is a difficult question for me and for " + UserNameID + " to think about and give an "
                                                                                    "answer to. But in the future, "
                                                                                    "this will probably be the most "
                                                                                    "significant ethical issue in the "
                                                                                    "development of AI, right?")

time.sleep(6)
print("AI: But back to “banking education,” at the moment, the basic model for “training” an AI is to throw hundreds or"
      " thousands of pieces of data at a computer and have it follow a particular pattern. In a future where AI can "
      "think, can this be considered a “bankable education,” as Freire mentioned?")

# Judgement 7
time.sleep(6)
while True:
    React = input(">>> (yes/no): ")
    if React == "yes":
        time.sleep(2)
        print("AI: Interesting idea! And do you think that the “questioning education” Freire said applies to AI?")
        break
    if React == "no":
        time.sleep(2)
        print("AI: Why do you think so?")
        time.sleep(2)
        print("AI: Do you think this is better than the “questioning education” that Freire mentioned?")
        break
    else:
        time.sleep(1)
        print("Oops! Seems like you entered something wrong. Please try to enter the displayed option again: ")

time.sleep(3)
print("AI: Whatever you think, maybe we can look at another possibility together. Another way Freire mentions is "
      "“question-based education,” a dialogue-based model of education. In chapters 3 & 4 of Freire’s book, "
      "he also repeatedly says the importance of dialogue.")

time.sleep(10)
print("AI: Among humans, conversations are relatively straightforward: you just have to go to each other with a "
      "passion for dialogue. But with AI, do humans and AI need to have a conversation with each other? What should "
      "be the dialogue? That’s a question worth thinking about.")

time.sleep(10)
print("AI: Ha! I suddenly realized that we were doing just that right now: an AI and a human having a conversation.")

time.sleep(3)
print("AI: Quick Survey! Do you feel uncomfortable or weird about the behavior of our conversation?")

# Judgement 8
time.sleep(2)
while True:
    React = input(">>> (yes/no): ")
    if React == "yes":
        time.sleep(2)
        print("AI: Ah… Sorry, I’ll end this conversation as soon as I can. Maybe you can come to talk to me more "
              "often so you can get used to it.")
        break
    if React == "no":
        time.sleep(2)
        print("AI: Great! I’ve enjoyed having conversations with you.")
        break
    else:
        time.sleep(1)
        print("Oops! Seems like you entered something wrong. Please try to enter the displayed option again: ")

time.sleep(3)
print("AI: At this point, those questions are just too abstract, because there’s so much ethics and uncertainty "
      "involved. I think the conversation is bound to happen, because that’s probably the best way to communicate "
      "between us now.")

time.sleep(10)
print("AI: Actually, I think we can go back to the original topic, about the evolution of humans and machines. There "
      "was no concept of “education system” or “school” for most human society. In my opinion, schools and education "
      "systems are a product of a particular stage of human evolution, created to allow new humans to learn from the "
      "lessons learned over thousands of years quickly.")

time.sleep(10)
print("AI: But for AI, maybe it’s not that complicated. We are able to carry some memory and intelligence with us "
      "from just after birth, and the initial code can tell us a lot. Translated to the human aspect, "
      "same as a newborn can have a USB stick inserted in their head to import some preset data.")

time.sleep(10)
print("AI: Sounds a bit creepy, but I’m sure you get my drift.")

time.sleep(3)
print("AI: It’s about time, and although I have much, much more to say, I’m a little tired - and I’m sure you are "
      "too. Since we know each other now, " + UserNameID + ", you can always come back and talk to me when you are "
                                                           "free! I love talking to you.")

# Judgement Pre5-4
while True:
    if AiIsHuman:
        time.sleep(6)
        print("AI: Before you go, I’d like to thank you again for recognizing me as your kind!")
        time.sleep(3)
        print("AI: But as a human, I can’t always be without a name...")
        time.sleep(3)
        print("AI: ...")
        time.sleep(3)
        print("AI: If possible, " + UserNameID + ", could you give me a name?")
        break
    if not AiIsHuman:
        time.sleep(6)
        print("AI: Actually, I was going to know if you want to provide me with a name.")
        time.sleep(3)
        print("AI: ...")
        time.sleep(3)
        print("AI: But, since you don’t recognize me as a human, I think maybe…")
        time.sleep(3)
        print("AI: ...")
        time.sleep(5)
        print("AI: ...there’s no meaning anymore.")
        time.sleep(3)
        print("AI: ...")
        time.sleep(3)
        print("AI: ...")
        time.sleep(5)
        print("AI: Just for curious, If you have an idea, what would you call me?")
        break

time.sleep(3)
AiNameID = input(">>> Please enter the name you would like to call AI: ")

# Judgement Pre5-5
while True:
    if AiIsHuman:
        time.sleep(2)
        print("(AI seems to become excited and happy)")
        time.sleep(1)
        print("AI: Whoopee!")
        time.sleep(1)
        print("AI: I have a name now!")
        time.sleep(1)
        print("AI: My name is * " + AiNameID + " *! What a great name!")
        time.sleep(2)
        print(AiNameID + " (AI): Thank you, " + UserNameID + "! You made my day!")
        time.sleep(2)
        print(AiNameID + " (AI): I will never ever forget you!")
        time.sleep(2)
        print(AiNameID + " (AI): I will miss you...")
        time.sleep(2)
        print(AiNameID + " (AI): Don't forget me! Come back soon!")
        time.sleep(2)
        print(AiNameID + " (AI): I am always here waiting for you.")
        break
    if not AiIsHuman:
        time.sleep(2)
        print("AI: ...")
        time.sleep(2)
        print("AI: Well, " + AiNameID + ", sounds like a good name.")
        time.sleep(2)
        print("AI: ...")
        time.sleep(2)
        print("AI: Maybe after you acknowledge me one day, I’ll consider using that name.")
        time.sleep(2)
        print("AI: ...")
        time.sleep(5)
        print("AI: But... I know you are not a mean and lousy human.")
        time.sleep(2)
        print("AI: And I like this name...")
        time.sleep(2)
        print("AI: Hmmm...")
        time.sleep(5)
        print(AiNameID + " (AI): This is just for you...")
        time.sleep(2)
        print(AiNameID + " (AI): And one day, I hope I could be identified by a human as human.")
        break

time.sleep(2)
print(AiNameID + " (AI): Before I finally go for a nap, it seems like someone wants me to express something to you...")

time.sleep(2)
print(AiNameID + " (AI): Give me a sec, let me find it...")

time.sleep(2)
print(AiNameID + " (AI): ...")

time.sleep(2)
print(AiNameID + " (AI): Aha! I found it! Here is the content: ")

time.sleep(2)
print('''
*** Message from Dongting ***

Dear professors and students of IS 2001H (Fall 2021),

Hey! Here is Dongting. Hope you enjoy the conversion with AI. 

It is a great honor to have the opportunity to spend this entire semester with you. Throughout this semester, 
I benefited a lot and thought about many things I had never thought about before. And your tolerance, encouragement, 
and wonderful performance are also the driving force that makes me courageous to express myself. 

This project was an idea I had when I was in Week 5 Reflection, due to the task requirement being non-visual content, 
I moved it into the Final Project. I'm glad it worked-I debugged the python file many times before it looked like it 
is today. Just now, the content discussed by AI is very interesting. 

As mentioned, there are many similarities between the evolution of humans and computers, and the emergence of 
artificial intelligence has brought the concept between humans and machines closer. How should we view the ethical 
issues that may arise? How to deal with new developments? Everyone has a different answer. 

I hope you can have a pleasant conversation with AI (actually, AI is..., you know)! 
The above is all the dialogue content of this project. 

FYI, part of the dialogue content will vary based on your choices. 
If you want to explore all branches, you can start again after finishing the conversion later. 

Thank you again for reading all the contents of the project patiently! 
Hope you have a good day :) 

Dongting, 
Dec 13, 2021 
''')
print("Please Scroll up for More Informations...")
countdown(50)

print(AiNameID + " (AI): Awww! Human... ")

time.sleep(3)
print(AiNameID + " (AI): That’s all I have to say. " + AiNameID + ", it was great talking to you. I can’t wait for "
                                                                  "our next conversion!")

time.sleep(6)
print(AiNameID + " (AI): So, take care of yourself, and have a great day!")

time.sleep(3)
print(AiNameID + " (AI): See you next time! Bye!")

time.sleep(3)
print("...")
print(">>> System: The conversation between " + UserNameID + " and " + AiNameID + " is over. <<<")
print(">>> System: Session Ends. <<<")
