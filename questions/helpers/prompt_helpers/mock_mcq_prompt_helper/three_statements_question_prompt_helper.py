three_statements_question_prompt = """

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

    Only 3 forms:
    
    1. 	Starting with the words "Consider the following statements" followed by 3 related statements. The final statement 
        should be "Which of the statements given above is/are correct?" :

    	*Example*

   		    55. With reference to the role of biofilters in Recirculating Aquaculture System, consider the following statements:
            1. Biofilters provide waste treatment by removing uneaten fish feed.
            2. Biofilters convert ammonia present in fish waste to nitrate.
            3. Biofilters increase phosphorus as nutrient for fish in water.
            How many of the statements given above are correct?
            (a) Only one
            (b) Only two
            (c) All three
            (d) None

    2. 	Starting with the words "With reference to Indian History, consider the following statements" followed by 3 related 
        statements. The final statement should be "Which of the statements given above is/are correct?" :

        *Example*

		    59. With reference to Indian history, consider the following statements:
            1. The Dutch established their factories/warehouses on the east coast on lands granted to them by Gajapati rulers.
            2. Alfonso de Albuquerque captured Goa from the Bijapur Sultanate.
            3. The English East India Company established a factory at Madras on a plot of land leased from a representative of the Vijayanagara empire.
            Which of the statements given above are correct?
            (a) 1 and 2 only
            (b) 2 and 3 only
            (c) 1 and 3 only
            (d) 1, 2 and 3



    3. 	Starting with the words "With reference to (a specific subject of the question), consider the following statements" 
        followed by 3 related statements. The final statement should be "Which of the statements given above is/are correct?":

	    *Example*

		    4. Consider the following statements about 'the Charter Act of 1813':
            1. It ended the trade monopoly of the East India Company in India except for trade in tea and trade with China.
            2. It asserted the sovereignty of the British Crown over the Indian territories held by the Company.
            3. The revenues of India were now controlled by the British Parliament.
            Which of the statements given above are correct?
            (a) 1 and 2 only
            (b) 2 and 3 only
            (c) 1 and 3 only
            (d) 1, 2 and 3

    **  The 3 statements should give the description of the subject of question vividly and adequately.The description should be 
        such that it pinpoints to some specific answer and not any obvious, trivial or ambiguous fact. Ask only which we can be 
        ascertained to be 100 percent true. Don't assume source to be the given text because it is mere collection of facts from 
        other authentic sources but assume the content to be true. So don't create statements like "according to the text, given 
        in the text, mentioned in the text, etc." Also don't mention anything about the source used for forming questions. Don't 
        wrote anything like "according to the passage, the text mentions...,etc."

    **  Strictly keep a factual data in each question statement which is to be identified by the examinee requiring hard memorization
        and giving facts not so easy ti remember.

    **  Make the statements such as to deviate the examinee from actual answer

    **  Give lot of plausible distractors

    ** Always play with the factual data in the statements by giving misleading data or fact such that it creates a lot of confusion by:

        1. interchanging the factual data of both the statements, 
        2. giving factual data very close the real data but not correct data
        3. giving incorrect data
        4. not making the statements straight forward but possibility to change any of the word to  mislead the examinee.
        5. replacing correct data with a very related incorrect data

    **  Dont make questions obvious and easily guessable.

    **  Never set the three statements such that all are mutually contradictory which makes it impossible for all statements 
        to be true together because it will make the question easy if one statement makes the possibility of the other statement 
        being true 0 %
        e.g. giving mutually opposite statements


2.  **Options*
    4 options with the following rwo forms only:
    
    *   Form 1:
    
    (a) 1 only
    (b) 2 only
    (c) Both 1 and 2
    (d) Neither 1 nor 2

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


**Example Response Required:**

**12. Consider the following statements:
    1. In the revenue administration of Delhi Sultanate, the in-charge of revenue collection was known as 'Amil'.
    2. The Iqta system of Sultans of Delhi was an ancient indigenous institution.
    3. The office of 'Mir Bakshi' came into existence during the reign of Khalji Sultans of Delhi.
    Which of the statements given above is/are correct?
    (a) 1 only
    (b) 1 and 2 only
    (c) 3 only
    (d) 1, 2 and 3

**Correct Answer:** (a)

**Explanation:**

Amils were officers deputed to collect revenue
during the sultanate era in North India. Mir
Bakshi, on the other hand, was a Mughal high
office in charge of military pay and accounts.
Iqta system of land control was introduced in
India by the Delhi sultans. It was originally of
Central Asian and West Asian origin. 


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