from django_elasticsearch_dsl import Document, fields
from django_elasticsearch_dsl.registries import registry
from .models import Shareholdershistory

@registry.register_document
class ShareholderDocument(Document):
    class Index:
        name = 'shareholders'
        settings = {
            'number_of_shards': 1,
            'number_of_replicas': 0
        }

    class Django:
        model = Shareholdershistory
        fields = ['symbol', 'shareholder_name', 'shareholder_percentage']
