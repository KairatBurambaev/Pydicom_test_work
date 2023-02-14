import pydicom as pm
import os

from glob import glob

path_to_dicom = 'src/*' # path to initial dicom file

def anonymize_dicom_and_save_in_new_structure(in_path, patient_name='anonymoys'):
    file_dicom = pm.dcmread(in_path)
    file_dicom.PatientName = patient_name
    # file anonymization

    new_path = f'tree/{file_dicom.StudyInstanceUID}/{file_dicom.SeriesInstanceUID}'
    os.makedirs(new_path, exist_ok="True")
    out_path = f'{new_path}/{file_dicom.SOPInstanceUID}.dcm'
    # creating an out path

    file_dicom.save_as(out_path)

    with open('description_of_the_new_structure.txt', 'a') as f:
        f.writelines(f'{in_path} --> {out_path}\n')
    # create file description change file path

for file in glob(path_to_dicom):
    anonymize_dicom_and_save_in_new_structure(file)