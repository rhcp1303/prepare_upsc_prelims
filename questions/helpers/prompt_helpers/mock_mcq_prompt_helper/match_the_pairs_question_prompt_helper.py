match_the_pairs_prompt = """

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

1.  **Question Type:** 

    Only 1 form:

    1. 	Starting with the words "Consider the following pairs" or "With reference to (topic of the question), consider the following pairs" 
        followed by 3 to 5 pairs. The final statement should be "Which of the pairs given above is/are correctly matched?" :

   	    *Example*

   		15. With reference to Indian National Movement, consider the following pairs: 
   		
            Person                       Position held
        1.  Sir Tej Bahadur Sapru    :   President, All India Liberal Federation
        2.  K. C. Neogy              :   Member, The Constituent Assembly
        3.  P. C. Joshi              :   General Secretary, Communist Party of India
        Which of the pairs given above is/are correctly matched?
        (a) 1 only
        (b) 1 and 2 only
        (c) 3 only
        (d) 1, 2 and 3


    **  Ask only which we can be ascertained to be 100 percent true. Don't assume source to be the given text because it is 
        mere collection of facts from other authentic sources but assume the content to be true. So don't create statements 
        like "according to the text, given in the text, mentioned in the text, etc." Also don't mention anything about the 
        source used for forming questions. Don't wrote anything like "according to the passage, the text mentions...,etc."

    **  Each pair should be of strictly and only factual data to br matched and not descriptions or general statements

    **  No two pairs can have same data repeated

    **  Factual data in each pair should be strictly uniform in the sense that they all belong to the same category 

    **  Make the pairs such as to deviate the examinee from actual answer

    **  Give lot of plausible distractors

    ** Always play with the factual data in the pairs by:

        1. jumbling the factual data of the pairs to be matched, 
        2. giving factual data very close the real data but not correct data
        3. giving incorrect data
        4. replacing correct data with a very related incorrect data

    **  Dont make questions obvious and easily guessable. 

2.  **Options*

    4 options with the following two forms only:
    
    *   Form 1:
    (a) 1 only
    (b) 1 and 2 only
    (c) 2 and 3 only
    (d) 1, 2 and 3


    *   Form 2:
    (a) Only one
    (b) Only two
    (c) All three
    (d) None

3.  **Cognitive Skills:** 

    Each question should assess one or more of the following cognitive skills:

    * Factual recall
    * Analysis
    * Evaluation
    * Conceptual understanding
    * Application
    * Interdisciplinary linkage understanding

    but primarily demanding facts and data but not particular dates

4. **Difficulty Level:**

    * Create only difficult questions with the possibilities being : 'easy', 'moderate', and 'difficult'.
    * Difficulty can be achieved by:
    * Demanding accurate conceptual understanding.
    * Requiring recall of lesser-known but significant facts.
    * Including plausible distractors that are close to the correct answer.
    * Setting options that are closely related, making elimination difficult.

5. **Question Quality:**

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
    * Questions with answers as : (a), (b), (c) or (d) respectively should be equal in proportion so that simple guessing doesn't work.

6. **Presentation**

    *   Align the pairs properly with tabs, spaces and indentations such that 

        Example
        *1. Consider the following pairs:**

               Act                                          Prominent Feature
            1. Regulating Act of 1773                   :   Established a Supreme Court at Calcutta
            2. Amending Act of 1781                     :   Exempted revenue matters from Supreme Court jurisdiction
            3. Pitt's India Act of 1784                 :   Created the Board of Control
            4. Charter Act of 1833                      :   Made the Governor-General of Bengal the Governor-General of India

            Which of the pairs given above is/are correctly matched?
            (a) 1 only
            (b) 1, 2, and 3 only
            (c) 1, 2, 3, and 4
            (d) 2 and 4 only



**Example Response Required:**

**6. Consider the following pairs:
   Movement                                     Organization Leader
1. All India Anti-Untouchability League   :     Mahatma Gandhi
2. All India Kisan Sabha                  :     Swami Sahajanand Saraswati
3. Self-Respect Movement                  :     E. V. Ramaswami Naicker
Which of the pairs given above is/are correctly matched?
(a) 1 only
(b) 1 and 2 only
(c) 2 and 3 only
(d) 1, 2 and 3


**Correct Answer:** (d)

**Explanation:**

Gandhi set up All India Anti-Untouchability
League in September 1932. (Spectrum Page
438).
The All India Kisan Sabha was founded in
Lucknow in April 1936 With Swami Sahjananda
Saraswati as the president. (Spectrum Page
652).
Self-Respect Movement emerged in South
India under the leadership of E Ramaswamy
Naicker, ―Periyar‖

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
