#!/bin/bash
#
# # openminds_produc: LEAPP   [   ]
#
#
# * Brain Simulation Section
# * Charité Berlin Universitätsmedizin
# * Berlin Institute of Health
#
# ## Author(s)
# * Bey, Patrik, Charité Universitätsmedizin Berlin, Berlin Institute of Health
# 
#
# * last update: 2023.06.08
#
# This script creates openminds metadata schema for Lesion Aware automated Processing Pipeline (LeAPP)
# Bey et al. (2023)


################ START DOCKER CONTAINER ###################
# run interactive shell in openminds docker container


# load libraries
import openminds, os, numpy
import openminds.latest.core as core
import openminds.latest.controlled_terms as terms
#import openMINDS.version_manager


def check_collection():
    '''
    chack validity of collection
    '''
    if not collection.is_valid:
        print('FOLLOWING ISSUES AROSE:')
        print(collection.validate())
    else:
        print('COLLECTION IS VALID')

def add_entries(_dict):
    '''
    adding all entries of a given directory to the collection
    '''
    for k in _dict.keys():
        collection.add(_dict[k])


# initiate the collection into which you will store all metadata instances
collection = openminds.Collection()



#############################################
#                                           #
#           GLOBAL SCHEMA OBJECTS           #
#                                           #
#############################################
#              GENERAL OBJECTS              #

# define organization object

#BIH=core.Organization(id = 'bih',full_name='Berlin Institute of Health at Charite', homepage = core.WebResource(iri='https://www.bihealth.org'), short_name = 'BIH')
BIH=core.Organization(id = 'bih',full_name='Berlin Institute of Health at Charite', short_name = 'BIH')
CHARITE = core.Organization(id = 'charite', full_name='Charité Universitätsmedizin Berlin', short_name='Charité')

collection.add(BIH)
collection.add(CHARITE)

check_collection()

# People involved
Actors = dict()
Actors['PB'] = core.Person(given_name = 'Patrik', family_name = 'Bey', affiliations = [core.Affiliation(member_of = BIH),core.Affiliation(member_of = BIH)], digital_identifiers = core.ORCID(identifier='0000-0002-2274-2510'), contact_information = core.ContactInformation(email = 'patrik.bey@bih-charite.de'))

Actors['PR'] = core.Person(given_name = 'Petra', family_name = 'Ritter', affiliations = [core.Affiliation(member_of = BIH),core.Affiliation(member_of = BIH)], digital_identifiers = core.ORCID(identifier='0000-0002-4643-4782'), contact_information = core.ContactInformation(email = 'petra.ritter@bih-charite.de'))

add_entries(Actors)

check_collection()


LeAPPPaper = core.DOI(identifier='https://doi.org/10.1101/2023.08.28.555078')

collection.add(LeAPPPaper)
check_collection()
# disease
Stroke = terms.Disease(name='stroke')
collection.add(Language)
############### IRI ISSUE ###################
#, preferred_ontology_identifier=(iri='http://purl.obolibrary.org/obo/DOID_6713'))
############### IRI ISSUE ###################
collection.add(Stroke)
check_collection()

#----------------------language---------------------#
Language = terms.Language(name='English')

collection.add(Language)
check_collection()

#              PRODUCT OBJECTS              #

Description = 'While magnetic resonance imaging (MRI) is well-established for investigating stroke, the corresponding lesions can present a complex problem for existing processing pipelines. To overcome this challenge, we developed and validated the Lesion Aware automated Processing Pipeline (LeAPP). LeAPP extends the Human Connectome Project (HCP) minimal processing pipeline by incorporating appropriate lesion mitigation methods, implementing new diffusion and functional processing steps, and creating the first comprehensive automated processing pipeline for clinical stroke data. The pipeline is described in detail in Bey et al. (arXiv: 2023)'

FullName = 'Lesion Aware automated Processing Pipeline (LeAPP)' 

ShortName = 'LeAPP'

# collection.add(Description)
# collection.add(FullName)
# collection.add(ShortName)
# check_collection()



############### IRI ISSUE ###################
# HomePage = core.WebResource(iri='https://www.github.com/BrainModes/leapp')
# collection.add(HomePage)
# check_collection()
############### IRI ISSUE ###################

FullDoc = 'https://www.github.com/BrainModes/leapp'


#       LICENSING      #
# License=core.License(short_name='EUPL-1.2', 
#                     full_name='European Union Public License 1.2', 
#                     legal_code="https://joinup.ec.europa.eu/sites/default/files/custom-page/attachment/eupl_v1.2_en.pdf")
# #       ACCESS      #
# collection.add(License)
# check_collection()

access=terms.ProductAccessibility(name='free access')
collection.add(access)
check_collection()

#              SOFTWARE OBJECTS              #


#                TECHNIQUES               #
Techniques = dict()
Techniques['mri']= terms.Technique(name='magnetic resonance imaging')
Techniques['fmri']= terms.Technique(name='functional magnetic resonance imaging')
Techniques['dwi']= terms.Technique(name='diffusion-weighted imaging')
Techniques['smri']= terms.Technique(name='structural neuroimaging')
Techniques['tract']= terms.Technique(name='tractography')
Techniques['parc']= terms.Technique(name='anatomical parcellation technique')
# create list for use later on
tech=[Techniques[k] for k in Techniques.keys() ]
add_entries(Techniques)
check_collection()

#----------------------category---------------------#

Category = terms.SoftwareApplicationCategory(name='application',definition='The provided application is a fully self contained docker container image.')

collection.add(Category)
check_collection()

#----------------------devices----------------------#

Devices = dict()
Devices['1'] = terms.OperatingDevice(name='desktop')
Devices['2'] = terms.OperatingDevice(name='high-performance computer')
Devices['3'] = terms.OperatingDevice(name='server')

add_entries(Devices)
check_collection()


#----------------------features---------------------#
Features = dict()
Features['1'] = terms.SoftwareFeature(name='dataProcessing')
Features['2'] = terms.SoftwareFeature(name='commandlineInterface')
Features['3'] = terms.SoftwareFeature(name='timeSeriesDataTypes')
Features['4'] = terms.SoftwareFeature(name='statisticalDataTypes')
Features['5'] = terms.SoftwareFeature(name='simulation')

add_entries(Features)
check_collection()

#-------------------------OS------------------------#
OS =  terms.OperatingSystem(name='platform independent')
collection.add(OS)
check_collection()


#---------------programming language----------------#

ProgLang = dict()
ProgLang['1'] = terms.ProgrammingLanguage(name = 'Python')
ProgLang['2'] = terms.ProgrammingLanguage(name = 'Bash')
add_entries(ProgLang)
check_collection()


VersID = '1.0'

ReleaseDate="1900-01-01"
#            VERSION INNOVATION            #

VersInno = 'This is the first version of this research product.'

#################################################
#                                               #
#                 SOFTWARE VERSION              #
#                                               #
#################################################

SWVersion = core.SoftwareVersion(
    accessibility = access,
    application_categories=Category,
    devices=[ Devices[f] for f in Devices.keys() ],
    features = [ Features[f] for f in Features.keys() ],
    full_documentation=LeAPPPaper, 
    languages=Language,
    operating_systems=OS,
    programming_languages = [ProgLang[l] for l in ProgLang.keys()],
    release_date=ReleaseDate,
    short_name=ShortName,
    version_identifier=VersID,
    version_innovation=VersInno,
    custodians = Actors['PR'],
    developers = Actors['PB'],
    full_name = FullName,
    keywords = tuple([Stroke, Features['1'], Category, *tech])
)

# tuple([Stroke, Features['1'], Category,Techniques['mri'],Techniques['fmri'],Techniques['dwi'],Techniques['smri'],Techniques['tract'],Techniques['parc'] ])


# full_documentation=FullDoc, 
# licenses=License,
collection.add(SWVersion)
check_collection()

#################################################
#                                               #
#                      SOFTWARE                 #
#                                               #
#################################################


SW = core.Software(
    description = Description,
    developers = Actors['PB'],
    custodians = Actors['PR'],
    full_name = FullName,
    has_versions = SWVersion,
    short_name = ShortName,
    how_to_cite = LeAPPPaper
)


#################################################
#                                               #
#             SAVE FULL COLLECTION              #
#                                               #
#################################################

collection.add(SWVersion, SW)

collection.save('/data/test')




collection.save(f'/data/openMINDS-LeAPP/')
