import tempfile

import pydicom
from pydicom.data import get_testdata_file

filename = get_testdata_file('0a67f9edb4915467ac16a565955898d3')
dataset = pydicom.dcmread(filename)

data_elements = ['PatientID',
                 'PatientBirthDate']
for de in data_elements:
    print(dataset.data_element(de))


