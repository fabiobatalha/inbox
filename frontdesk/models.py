from django.db import models
from django.urls import reverse

from model_utils.models import TimeStampedModel
from model_utils.fields import StatusField, MonitorField
from model_utils import Choices


class Deposit(TimeStampedModel):
    """O depósito de um pacote SciELO PS para ingresso na coleção.

    A mudança de estados do pacote -- esperando análise, aceito e rejeitado --
    é implementada pela instância de ``StatusField``, uma máquina de estados
    finitos extremamente simplificada.

    A superclasse ``TimeStampedModel`` provê os atributos ``created`` e
    ``modified``, contendo a data e hora de criação e de modificação da
    entidade, respectivamente.

    Mais informação sobre ``StatusField`` e ``TimeStampedModel`` em:
    https://django-model-utils.readthedocs.io/en/latest/
    """
    STATUS = Choices('deposited', 'rejected', 'accepted')

    status = StatusField()
    status_changed = MonitorField(monitor='status')
    depositor = models.CharField(max_length=16)


class Package(TimeStampedModel):
    """Pacote depositado para inclusão na coleção.

    Um pacote é basicamente um maço, zipado, de arquivos XML -- que devem ser
    válidos em relação a especificação SciELO PS -- e seus respectivos ativos
    digitais, incluindo PDF.

    A superclasse ``TimeStampedModel`` provê os atributos ``created`` e
    ``modified``, contendo a data e hora de criação e de modificação da
    entidade, respectivamente.

    Mais informação sobre ``TimeStampedModel`` em:
    https://django-model-utils.readthedocs.io/en/latest/
    """
    deposit = models.OneToOneField(Deposit, on_delete=models.CASCADE,
            related_name='package')
    file = models.FileField(upload_to='packages/%Y/%m/%d/', max_length=1024)
    md5_sum = models.CharField(max_length=32)  # 32 dígitos hexadecimais

