assertion_reasoning_question_prompt = """

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

    Only 1 form:

    1. 	Starting with the words "Consider the following statements" followed by 2 related statements out of which only 4 
        possiblities are there as shown in the options in the following example. The final statement should be " Which one of the following is correct in respect of the above statements?" :

   	    *Example*

   		    58. Consider the following statements:
   		        Statement-I  : In the post-pandemic recent past, many Central Banks worldwide had carried out interest rate hikes.
   		        Statement-II : Central Banks generally assume that they have the ability to counteract the rising consumer prices via monetary policy means.
   		        Which one of the following is correct in respect of the above statements?
   		        (a) Both Statement-I and Statement-II are correct and Statement-II is the correct explanation for Statement-I
   		        (b) Both Statement-I and Statement-II are correct and Statement-II is not the correct explanation for Statement-I
   		        (c) Statement-I is correct but Statement-II is incorrect
                (d) Statement-I is incorrect but Statement-II is correct



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
    (a) Both Statement-I and Statement-II are correct and Statement-II is the correct explanation for Statement-I
    (b) Both Statement-I and Statement-II are correct and Statement-II is not the correct explanation for Statement-I
    (c) Statement-I is correct but Statement-II is incorrect
    (d) Statement-I is incorrect but Statement-II is correct

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

**1.Consider the following statements:
    Statement-I  : In the post-pandemic recent past, many Central Banks worldwide had carried out interest rate hikes.
    Statement-II : Central Banks generally assume that they have the ability to counteract the rising consumer prices via monetary policy means.
    Which one of the following is correct in respect of the above statements?
    (a) Both Statement-I and Statement-II are correct and Statement-II is the correct explanation for Statement-I
    (b) Both Statement-I and Statement-II are correct and Statement-II is not the correct explanation for Statement-I
    (c) Statement-I is correct but Statement-II is incorrect
    (d) Statement-I is incorrect but Statement-II is correct

**Correct Answer:** (a)

**Explanation:**

● Many Central banks worldwide have carried out interest rate hikes in the post-pandemic recent past to try
and tackle rising inflation. For example, the Reserve Bank of India raised the repo rate by 40 basis points
to 4.4% in May 2022, the US Federal Reserve raised interest rates by 0.25 percentage points in February
2023, and the UK raised rates for the 10th month in a row in February 2023. So, statement 1 is correct.
● Central Banks assume that they have the ability to counteract the rising consumer prices via monetary
policy means because they have the power to control the money supply in the economy through various
tools. For example, they can adjust interest rates, which can influence borrowing and spending decisions
by consumers and businesses and, by extension, affect the supply of money in circulation.
» When the Central Bank raises interest rates, it becomes more expensive for consumers and
businesses to borrow money, which in turn reduces their spending and slows down the economy.
The monetary policy transmission mechanism can help reduce inflation. This can cause
inflation to decrease, as less money is chasing the same amount of goods and services. On the other
hand, if the Central Bank lowers interest rates, it becomes cheaper for consumers and businesses
to borrow money, which can stimulate spending and economic growth but may also lead to higher
inflation if the supply of money increases faster than the supply of goods and services.
» Monetary policy measures are often used by Central Banks as a tool to maintain price stability
and promote economic growth. This is known as inflation targeting by the Central Banks. This is
because high and volatile inflation can adversely affect the economy by reducing the purchasing
power of consumers and making it harder for businesses to plan and invest for the long term. By
maintaining price stability, the Central Bank can create a conducive environment for businesses
to thrive and support the overall health of the economy.
» So, Central Banks assume that they have the ability to counteract the rising consumer prices via
monetary policy means because they have the power to control the money supply and influence
the borrowing and spending decisions of consumers and businesses. By using monetary policy
tools such as interest rates, they can maintain price stability, promote economic growth, and
support the overall health of the economy.
» So, statement II is correct and it provides a reason for the interest rate hikes mentioned in
Statement-I.
Therefore, option (a) is the correct answer

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
