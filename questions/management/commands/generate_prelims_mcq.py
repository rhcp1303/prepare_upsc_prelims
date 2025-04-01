from django.core.management.base import BaseCommand
from ...helpers import generate_prelims_mcq_from_questions_helper as helper
import logging

logger = logging.getLogger(__name__)


class Command(BaseCommand):
    help = 'Generate mcqs for upsc prelims mock test'

    def add_arguments(self, parser):
        parser.add_argument('--source_embeddings_path', type=str, help='path to the guide faiss folder', required=True)
        parser.add_argument('--target_embeddings_path', type=str,
                            help='path to the faiss folder from where mcqs are to be generated', required=True)
        parser.add_argument('--prefix', type=str,
                            help='prefix (containing subject name and year if current affairs) to be used for the file name containing generated mcqs',
                            required=True)

    def handle(self, *args, **options):
        source_embeddings_path = options['source_embeddings_path']
        target_embeddings_path = options['target_embeddings_path']
        prefix = options['prefix']
        logger.info(f"Starting generation of of questions:")
        helper.generate_mock_mcq(source_embeddings_path, target_embeddings_path, prefix)
