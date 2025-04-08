from django.core.management.base import BaseCommand
import logging
from ...helpers import generate_explanaton_helper as helper

logger = logging.getLogger(__name__)


class Command(BaseCommand):
    help = 'This is a utility management command for testing purpose'

    def handle(self, *args, **options):
        source_question = '''

**1. Consider the following statements regarding Nagarjuna:**

1. He is primarily associated with the Mahayana school of Buddhism.
2. His birthplace is traditionally identified with Gujarat.
3. He made significant contributions to the field of alchemy.
4.  The archaeological site of Nagarjunakonda is named after him.

How many of the above statements are factually accurate?

(a) Only one
(b) Only two
(c) Only three
(d) All four
        '''

        source_embeddings_path = "questions/data/faiss_folder/consolidated_target_index/complete_history_art_and_culture.faiss"
        helper.generate_explanation(source_question, source_embeddings_path)
        print("here")
