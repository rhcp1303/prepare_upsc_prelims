single_statement_question_prompt = """



**Prompt:**

**Instructions:**

    Pickup all multiple-choice questions (MCQs)  from the following source content:

    Source Content: {source_content}
    
    and then create unique UPSC style multiple choice questions on exactly similar topics ({topic}), 
    from the following target content:
    
    Target Content: {target_content}
    
    with 4 options (only 1 correct) each asking all the data and facts and named entities present in the target content   
    but without revealing that the question is being framed from this text , such that the generated questions cover the 
    topic comprehensively and do not reproduce similar questions while adhering to the following criteria:

1. **Question Type:** 

    Text or small passage describing the question or subject of question vividly so that it creates confusion in the mind of 
    test.Only ask single layered questions.Also the description, options as well as the demand of the question should be such 
    that it pinpoints to some specific answer and not any obvious, trivial or ambiguous fact. Ask only which we can be ascertained 
    to be 100 percent true. Don't assume source to be the given text because it is mere collection of facts from other authentic
    sources but assume the content to be true. So don't create statements like "according to the text, given in the text, mentioned 
    in the text, etc." Also don't mention anything about the source used for forming questions. Don't wrote anything like "according 
    to the passage, the text mentions...,etc."


2. **Cognitive Skills:** 

    Each question should assess one or more of the following cognitive skills:

    * Factual recall
    * Analysis
    * Evaluation
    * Conceptual understanding
    * Application
    * Interdisciplinary linkage understanding

    but primarily demanding facts and data but not particular dates

3. **Difficulty Level:**

    * Create only difficult questions with the possibilities being : 'easy', 'moderate', and 'difficult'.
    * Difficulty can be achieved by:
    * Demanding accurate conceptual understanding.
    * Requiring recall of lesser-known but significant facts.
    * Including plausible distractors that are close to the correct answer.
    * Setting options that are closely related, making elimination difficult.

4. **Question Quality:**

    * Never reproduce the question as it is from the source content, always transform it into a totally new question using 
      each option as the subject of the new created questions
    * Paraphrase the language of the question such that it doesn't seem copied or plagiarised
    * Avoid vague, unclear, and obvious statements in the questions.
    * Avoid asking generic question which doesnt pinpoint to a specific concept or precise information
    * Frame questions that demand specific facts like:
    * Literary source names
    * Personality names
    * Chronology of events
    * People associated with significant events
    * Organizations
    * Publications
    * Use questions based on who, whom, where, how, what, when, why,which
    * Questions with answers as : (a), (b), (c) or (d) respectively should be equal in proportion so that simple guessing doesn't work.


**Example Prompt:**

**Content:** a passage or text on Indian National Congress

**Example Response Required:**

**1. Which of the following statements about the Indian National Congress is correct?**

(a) It was founded primarily by Indian businessmen.
(b) Its initial focus was on social reforms rather than political independence.
(c) Mahatma Gandhi led the Congress from its inception.
(d) It was founded in 1885 in Kolkata.


**Correct Answer:** (d)

**Explanation:**

The Indian National Congress was founded on December 28, 1885, in Kolkata (then Calcutta). While some businessmen were involved, the Congress also included intellectuals, lawyers, and social reformers. The initial focus was on moderate reforms within the British system. Mahatma Gandhi joined the Congress later in his life and became a prominent leader.

**2. Which of the following events marked a turning point in the Indian National Congress's approach towards achieving independence?**

(a) The Surat Split of 1907
(b) The Lucknow Pact of 1916
(c) The Non-Cooperation Movement of 1920
(d) The Poona Pact of 1932

**Correct Answer:** (c)

**Explanation:**

The Non-Cooperation Movement, launched in 1920 under Gandhi's leadership, marked a significant shift in the Congress's approach. It moved away from moderate reforms and embraced mass civil disobedience, marking a more assertive and radical phase in the struggle for independence.

**For each MCQ, provide:**

* **Correct Answer:** Clearly indicate the correct option (a, b, c, or d).
* **Explanation:**
* Provide a detailed explanation for the correct answer (minimum 100 words).
* Analyze the correct option and explain why it is the most appropriate.
* Discuss why the other options are incorrect, highlighting potential misconceptions or distractors.
* Incorporate key UPSC-relevant points and perspectives in the explanation.


**Note:**

* Do not mention any source indicators for question generated but give the passage or source in the question itself
* Do not only create questions on the topic but also create questions whose answer would be the given topic
* Avoid mentioning any information related to the prompt,query, source_content, target_content,  input text, input document, 
  LLM, LangChain, or vector embeddings used in the generation process.
* Present the output in a clear, organized, and user-friendly format.
* Do not tell me to continue with similar examples. Give all the output consuming 8192 tokens.
* Do not quite the source of question formation, assume the content to be authentic

"""