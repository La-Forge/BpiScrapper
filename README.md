# BpiScrapper
Extract companies data from the BPI website

## Dependency requirements:

* selenium (tested with 3.141.0)

Selenium needs a webdriver to work; more information, proper installation instructions and documentation are available [here](https://selenium-python.readthedocs.io/installation.html) and [here](https://pythonspot.com/selenium-webdriver/).

## Example

Extract for one company
```python
from BpiScrapper import Company
from pprint import pprint

company = Company("https://lehub.web.bpifrance.fr/startup/askhub")
pprint(company.getData())
```

Result
'''
{'identity': {'adress': '9 RUE DAREAU\nPARIS 14\n75014 France',
              'business_model': ['B2B', 'SAAS'],
              'creation': '2017',
              'description': 'Experte du traitement automatique du langage '
                             '(TALN) ou Natural Language Processing (NLP), '
                             'AskHub automatise les canaux conversationnels '
                             '(livechats, emails, appels téléphoniques), '
                             'améliore les agents conversationnels (chatbots, '
                             'voicebots, IVRs...) et permet aux entreprises de '
                             'piloter leur performance conversationnelle. \n'
                             '\n'
                             'L’objectif est de générer des gains en termes de '
                             'rapidité de réponse, de taux de conversion, '
                             "d'économies de coûts et de satisfaction client.",
              'headcount': '7',
              'jobs': ['DSI / SÉCURITÉ', 'MARKETING / COMMUNICATION'],
              'linkedin': 'https://www.linkedin.com/company/askhub/',
              'locations': [],
              'logo': 'https://storage.gra.cloud.ovh.net/v1/AUTH_5b52b2f4ab714e20821799649e702a79/production-hubdigital-medias/awsS3-uploads/329aadbc9a2136abe3fe255bab658c0d',
              'market': ['AGRO-ALIMENTAIRE',
                         'ASSURANCE',
                         'AUTOMOBILE',
                         'BANQUE / FINANCE',
                         'CONSUMER GOODS',
                         'DISTRIBUTION',
                         'EDUCATION / FORMATION',
                         'ENERGIE',
                         'GOUVERNEMENT',
                         'IMMOBILIER',
                         'MEDIA & DIVERSTISSEMENT',
                         'PROFESSIONAL SERVICES',
                         'SANTÉ / PHARMACIE',
                         'SERVICES PUBLICS',
                         'TECHNOLOGIE & TELECOMMUNICATIONS',
                         'TRANSPORT',
                         'VOYAGE / TOURISME'],
              'name': 'ASKHUB',
              'siren': '829785476',
              'technologies': ['API', 'INTELLIGENCE ARTIFICIELLE', 'SOFTWARE'],
              'twitter': 'https://twitter.com/AskHub_io',
              'website': 'https://www.askhub.io/'},
 'products': {'description': 'AskHub est une solution SaaS qui génère des '
                             'insights actionnables pour améliorer les '
                             'capacités et l’UX des agents conversationnels '
                             "(chatbots et voicebots) afin d'optimiser leur "
                             'ROI.\n'
                             '\n'
                             'Nos algorithmes propriétaires permettent à nos '
                             'clients :\n'
                             "=> d'accélérer l'entrainement de leur bot\n"
                             "=> d'identifier les besoins des utilisateurs en "
                             'analysant leurs requêtes\n'
                             '=> de comprendre comment les utilisateurs '
                             'interagissent avec leur bot\n'
                             "=> d'analyser les parcours utilisateurs pour "
                             'maximiser le ROI du bot',
              'title': 'Logiciel SaaS AskHubRéduire'},
 'team': [{'function': 'Co-founder', 'name': 'Mathieu Rouxel'}]}
 '''

## Disclaimer
The scrapper presented here are proposed for experimentation purposes only. Please be advised that tools designed to automatically fetch data may be incompatible with the terms of use of some website.
