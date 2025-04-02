from django.core.management.base import BaseCommand
import logging
from ...helpers import generate_prelims_mcq_from_questions_helper as helper

logger = logging.getLogger(__name__)


class Command(BaseCommand):
    help = 'This is a utility management command for testing purpose'

    def handle(self, *args, **options):
        source_question = '''
        Which one of the following statements about Sangam literature in ancient South India is correct?

a) Sangam poems are devoid of any reference to material culture.

b) The social classification of Varna was known to Sangam poets.

c) Sangam poems have no reference to warrior ethic.

d) Sangam literature refers to magical forces as irrational.
        '''
        target_embeddings_path = "questions/data/faiss_folder/consolidated_target_index/complete_history_art_and_culture.faiss"
        helper.generate_mock_mcq(source_question, target_embeddings_path, "temp")
        print("here")
