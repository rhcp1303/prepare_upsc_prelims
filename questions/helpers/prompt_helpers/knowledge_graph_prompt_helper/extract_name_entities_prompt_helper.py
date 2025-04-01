named_entity_prompt = """
    Identify named entities in the following text that are relevant to the UPSC syllabus.
    Text:
    {text}

    Provide the entities as a JSON list of dictionaries, where each dictionary has "entity" (the exact text of the entity) and "label".
    Only include entities that are highly relevant to the UPSC context.

    **Instructions**:
    1. Give the output without any backtick.

    Example Output:
    [
      {{ "entity": "Mahajanapadas", "label": "HISTORICAL_PERIOD" }},
      {{ "entity": "Indian Constitution", "label": "POLITICAL_DOCUMENT" }},
      {{ "entity": "Article 370", "label": "CONSTITUTIONAL_ARTICLE" }},
      {{ "entity": "Paris Agreement", "label": "INTERNATIONAL_AGREEMENT" }},
      {{ "entity": "Bhimbetka", "label": "ARCHAEOLOGICAL_SITE" }}
    ]
    """