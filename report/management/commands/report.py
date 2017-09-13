#coding:utf-8

from django.core.management.base import BaseCommand

from wkhtmltopdf.utils import render_pdf_from_template

from django.template.loader import get_template

class Command(BaseCommand):

    def handle(self, *args, **options):

        title =  'Hello World fú'

        template = get_template('report/report.html')

        pdf_content = render_pdf_from_template(template,
            header_template=None,
            footer_template=None,
            context={'foo': title}
        )

        with open('arquivo.pdf', 'w') as arquivo:
            arquivo.write(pdf_content)