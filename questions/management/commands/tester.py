from django.core.management.base import BaseCommand
import logging
from ...helpers import get_named_entities_from_text_helper as helper

logger = logging.getLogger(__name__)


class Command(BaseCommand):
    help = 'This is a utility management command for testing purpose'

    def handle(self, *args, **options):
        text = '''
        1. Consider the following statements regarding the Association of Southeast Asian Nations (ASEAN):
1. It is a regional grouping of twelve
members incuding India.
2. ASEAN Defence Ministers’ Meeting -
Plus (ADMM-Plus) is the highest defence consultative and cooperative mechanism in ASEAN.
Which of the statements given above is/are correct?
(a) 1 only
(b) 2 only
(c) Both 1 and 2 (d) Neither 1 nor 2

        
        '''
        ne = helper.get_ner_labels_from_llm(text)
        print(ne)
        print("here")
