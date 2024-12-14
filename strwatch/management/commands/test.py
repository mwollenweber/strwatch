import logging
import requests
from django.core.management.base import BaseCommand
from csv import reader
from io import BytesIO, StringIO

from strwatch.settings import DATA_URL
from strwatch.models import STRrecord

logger = logging.getLogger(__name__)


class Command(BaseCommand):
    def handle(self, **options):
        print(f"test")
        logging.info("test")

        res = requests.get(DATA_URL)
        res.raise_for_status()

        f = StringIO(res.text)
        csv_reader = reader(f)
        for row in csv_reader:
            try:
                permit_number = row[0]
                address = row[1]
                permit_type = row[2]
                residential_subtype = row[3]
                current_state = row[4]
                expired = row[5]
                expiration_date = row[6]
                bedroom_limit = row[7]
                guest_limit = row[8]
                link = row[9]
                operator_name = row[10]
                operator_phone = row[11]
                operator_email = row[12]
                operator_permit_number = row[13]
                license_holder_name = row[14]
                application_date = row[15]
                issue_date = row[16]
                reference_code = row[17]

                #print(f"{reference_code}")
                STRrecord.objects.create(
                    permit_number=permit_number,
                    address=address,
                    permit_type=permit_type,
                    residential_subtype=residential_subtype,
                    expired=expired,
                    #expiration_date=expiration_date,
                    #bedroom_limit=bedroom_limit,
                    #guest_limit=guest_limit,
                    link=link,
                    operator_name=operator_name,
                    operator_phone=operator_phone,
                    operator_permit_number=operator_permit_number,
                    license_holder_name=license_holder_name,
                    #application_date=application_date,
                    #issue_date=issue_date,
                    reference_code=reference_code
                )

            except Exception as e:
                logger.error(e)
