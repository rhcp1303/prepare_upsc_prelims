two_statements_question_prompt = """

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

2.  **Question Type:** 

    Only 3 forms:
    
    1. 	Starting with the words "Consider the following statements" followed by 2 related statements out of which only 4 
        possiblities are there as shown in the options in the following example. The final statement should be "Which of the 
        statements given above is/are correct?" :

   	    *Example*

   		    58. Consider the following statements:
		    1. In the tropical zone, the western sections of the oceans are warmer than the eastern sections owing to the influence of trade winds.
		    2. In the temperate zone, westerlies make the eastern sections of oceans warmer than the western sections.
		    Which of the statements given above is/are correct?
		    (a) 1 only
		    (b) 2 only
		    (c) Both 1 and 2
		    (d) Neither 1 nor 2

    2. 	Starting with the words "With reference to Indian History, consider the following statements" followed by 2 related 
        statements out of which only 4 possiblities are there as shown in the options in the following example. The final 
        statement should be "Which of the statements given above is/are correct?" :

        *Example*

		    59. With reference to Indian history, consider the following statements:
		    1. The Dutch established their factories/warehouses on the east coast on lands granted to them by Gajapati rulers.
		    2. Alfonso de Albuquerque captured Goa from the Bijapur Sultanate.
		    Which of the statements given above are correct?
		    (a) 1 only
		    (b) 2 only
		    (c) Both 1 and 2
		    (d) Neither 1 nor 2


        3. 	Starting with the words "With reference to (a specific subject of the question), consider the following statements" followed by 2 related statements out of 
	    which only 4 possiblities are there as shown in the options in the following example. The final statement should be "Which of the statements given above is/are correct?":

	    *Example*

		    10. With reference to Swadeshi Movement, consider the following statements:
		    1. It contributed to the revival of the indigenous artisan crafts and industries.
		    2. The National Council of Education was established as a part of Swadeshi Movement.
		    Which of the statements given above is/are correct?
		    (a) 1 only
		    (b) 2 only
		    (c) Both 1 and 2
		    (d) Neither 1 nor 2

    **  The 2 statements should give the description of the subject of question vividly and adequately.The description should be 
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

    **  Never set the two statements such that both are mutually contradictory which makes it impossible for both statements to be true together
        because it will make the question easy if one statement makes the possibility of the other statement being true 0 %
        e.g. giving mutually opposite statements


2.  **Options*
    4 options with the following forms only and strictly:
    (a) 1 only
    (b) 2 only
    (c) Both 1 and 2
    (d) Neither 1 nor 2

3.    **Cognitive Skills:** 

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

**1. With reference to the proposals of Cripps Mission, consider the following statements:
    1. The Constituent Assembly would have members nominated by the Provincial Assemblies as well as the Princely States.
    2. Any Province, which is not prepared to accept the new Constitution would have the right to sign a separate agreement     
       with Britain regarding its future status.
    Which of the statements given above is/are correct?**
    (a) 1 only
    (b) 2 only
    (c) Both 1 and 2
    (d) Neither 1 nor 2

**Correct Answer:** (b)

**Explanation:**

● In March 1942, a mission headed by Stafford Cripps was sent to India with constitutional
proposals to seek Indian support for the war.
● It proposed that the Constituent Assembly was to be composed of elected (and not
nominated) members from provinces. Only the section representing the Princely states was
to be nominated. So, statement 1 is not correct.
● It also stated that if any Province which is not prepared to accept the new Constitution would
have the right to sign a separate agreement with Britain regarding its future status. This
became the primary reason for the failure of the Cripps mission as this provision allowed for
balkanization of India. So, statement 2 is correct.



**2. Consider the following statements:
    1. The Montagu-Chelmsford Reforms of 1919 recommended granting voting rights to all the women above the age of 21.
    2. The Government of India Act of 1935 gave women reserved seats in the legislature.
    Which of the statements given above is/are correct?
    (a) 1 only
    (b) 2 only
    (c) Both 1 and 2
    (d) Neither 1 nor 2**

**Correct Answer:** (d)

**Explanation:**

Statement 1 is incorrect. The Montague Chelmsford reforms of 1919 did not recommend granting voting rights
to all women above the age of 21. Although it recommended the voting rights to women in limited numbers
to be extended on the basis of property, tax or education.
Statement 2 is incorrect. The Government of India Act 1935 gave women separate electorate (and did not
reserved seats for women in legislature). It provided separate electorates to depressed classes and labours also.


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