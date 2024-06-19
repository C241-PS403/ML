## Completing Data Collection and Preprocessing 
## Completing Model Building and Tuning
## Completing Model Deployment

- Data collection was done using the kaggle website.
- Data preprocessing has been done using image resize, image normalize and image augmentation techniques.
- Data Resize has been performed by converting various different image sizes to the same size of 224 x 224 px.
- Data Normalization has been performed to change the range of pixel value ranges.
- Data Contrast Enhancement has been collected to enhance the color contrast of the dataset.
- Data Augmentation has been performed to augment photos with various photo models.
- Split Data was used with parameters 70% for training data, 20% for test data and 10% for val data. 

- Data Detail:
  
  # Data Train  : 
    - Geblek Renteng  : 98 Images
    - Gentongan       : 98 Images
    - Liong           : 98 Images
    - Mega Mendung    : 98 Images
    - Parang          : 98 Images
    - Sekar Jagad     : 98 Images
    - Sidomukti       : 98 Images
    - Tambal          : 98 Images
    - Truntum         : 98 Images
    - Tujuh Rupa      : 98 Images
  
  # Data Val    :
    - Geblek Renteng  : 14 Images
    - Gentongan       : 14 Images
    - Liong           : 14 Images
    - Mega Mendung    : 14 Images
    - Parang          : 14 Images
    - Sekar Jagad     : 14 Images
    - Sidomukti       : 14 Images
    - Tambal          : 14 Images
    - Truntum         : 14 Images
    - Tujuh Rupa      : 14 Images

  # Data Test  :
    - Geblek Renteng  : 28 Images
    - Gentongan       : 28 Images
    - Liong           : 28 Images
    - Mega Mendung    : 28 Images
    - Parang          : 28 Images
    - Sekar Jagad     : 28 Images
    - Sidomukti       : 28 Images
    - Tambal          : 28 Images
    - Truntum         : 28 Images
    - Tujuh Rupa      : 28 Images

- The model has been built using customised models and adapted by our own dataset and MobileNetV2-based model architecture.

- Model is saved in HDF5 format
- Model is deployed with Flask
- Model is deployed in Google Cloud Platform
- Model is deployed using CI/CD cycle and Docker